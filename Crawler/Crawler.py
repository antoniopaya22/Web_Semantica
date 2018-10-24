# -*- coding: utf-8 -*-

#=========================================================
# Clase Crawler
#
# Autor: Antonio Paya Gonzalez
#
#=========================================================
from __future__ import print_function
from __future__ import unicode_literals

from bs4 import BeautifulSoup
from urlparse import urlparse, urljoin

import requests
import time
import robotparser


class Crawler(object):
    def __init__(self, max_downloads, seconds, name):
        """Constructor Crawler

        Params:
            max_downloads, int con el numero de max_downloads
            seconds, int con el numero de segundos
            name, nombre del crawler
        """
        self.max_downloads = max_downloads
        self.seconds = seconds
        self.name = name
        self.visit_url = []

    def scan_a(self, links, max_downloads, url, base):
        """Escaneo en anchura

        Params:
            links, lista con todas las urls
            max_downloads, int con el numero de max_downloads
            url, url a escanear
            base, url base a escanear
        """
        if url in self.visit_url or self.max_downloads == 0:
            return
        if not self.scanRobots(base, url):
            return
        r = requests.get(url, headers={"User-Agent": "crawler_v1"})
        time.sleep(self.seconds)
        if "text/html" not in r.headers["Content-Type"] or r.status_code != 200:
            return
        self.max_downloads -= 1
        self.visit_url.append(url)
        print("(ok) Crawling {} ,Max downloads {}".format(url,self.max_downloads))
        s = BeautifulSoup(r.text, "html.parser")
        enlaces = s.find_all('a', href=True)
        for l in enlaces:
            l = self.normalize_link(l.get("href"), url)
            if l is None:
                continue
            links.pop(0)
            links.append(l)
            self.scan_a(links, max_downloads, links[0], links[0])

    def scan_p(self,url,base):
        """Escaneo en profundidad

        Params:
            url, url a escanear
            base, url base a escanear
        """
        if url in self.visit_url or self.max_downloads == 0:
            return
        if not self.scanRobots(base, url):
            return
        r = requests.get(url, headers={"User-Agent": "crawler_v1"})
        time.sleep(self.seconds)
        if "text/html" not in r.headers["Content-Type"] or r.status_code != 200:
            return
        self.max_downloads -= 1
        self.visit_url.append(url)
        print("(ok) Crawling {} ,Max downloads {}".format(url,self.max_downloads))
        s = BeautifulSoup(r.text, "html.parser")
        links = s.find_all('a', href=True)
        for l in links:
            l = self.normalize_link(l.get("href"), url)
            if l is None:
                continue
            self.scan_p(l,l)

    def normalize_link(self, url, base):
        """Normariza la url

        Params:
            url, url a normalizar
            base, url base a normalizar
        """
        if url.startswith("javascript:"):
            return None
        if url.startswith("/") or url.startswith("#"):
            url = urljoin(base, url)
        if "https://" in url:
            url = url.replace("http://","https://")
        if "//" in url.replace("https://", ""):
            url = "http://" + (url.replace("http://", "").replace('//','/'))
        return url

    def scanRobots(self,url,link):
        """ScanRobots

        Revisa el robots.txt y devuelve True en caso de que se pueda
        escanear la web y False en caso contrario

        Params:
            url, url base
            link, url a comprobar por robots.txt
        """
        url = urlparse(url)
        base = url[0] + '://' + url[1]
        if base.endswith('/'):
            base = base[:len(base)-1]
        robots_url = urljoin(base, '/robots.txt')

        self.robot_parser = robotparser.RobotFileParser()
        self.robot_parser.set_url(robots_url)
        self.robot_parser.read()
        time.sleep(self.seconds)

        if not self.robot_parser.can_fetch(self.name, link.encode('utf-8')):
            print("(!) Cannot scrap {}".format(link))
            print ("\t # Crawling {} is prohibited unless you have express written".format(link))
            return False
        return True
