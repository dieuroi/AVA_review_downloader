#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/1 12:26
# @Author  : dieuroi
# @Site    : 
# @File    : xslt_lib.py
# @Software: PyCharm
no_author = """\
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:svg="http://www.w3.org/2000/svg" >
    <xsl:template match="/">
    <noAuthor>
    <xsl:apply-templates select="//*[@class='textsm']/table[position()=2]/tbody/tr/td[position()=2]/table[position()=3]/tbody/tr[position()=2]/td/b[count(./.)>0]" mode="noAuthor"/>
    </noAuthor>
    </xsl:template>


    <xsl:template match="//*[@class='textsm']/table[position()=2]/tbody/tr/td[position()=2]/table[position()=3]/tbody/tr[position()=2]/td/b[count(./.)>0]" mode="noAuthor">
    <item>
    <label>
    <xsl:value-of select="."/>
    </label>
    </item>
    </xsl:template>
    </xsl:stylesheet>"""


ur_no_author = """\
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
    <xsl:template match="/">
    <ur>
    <xsl:apply-templates select="//*[@class='textsm']/table[position()=2]/tbody/tr/td[position()=2]/table[position()=3]/tbody/tr[position()>=3 and ((position()-3) mod 3)=0 and count(.//*/@href)>0 and count(./following-sibling::tr[position()=1]/td/table/tbody/tr/td/text())>0]" mode="ur"/>
    </ur>
    </xsl:template>


    <xsl:template match="//*[@class='textsm']/table[position()=2]/tbody/tr/td[position()=2]/table[position()=3]/tbody/tr[position()>=3 and ((position()-3) mod 3)=0 and count(.//*/@href)>0 and count(./following-sibling::tr[position()=1]/td/table/tbody/tr/td/text())>0]" mode="ur">
    <item>
    <user>
    <xsl:value-of select="*//*/@href"/>
    <xsl:value-of select="*/@href"/>
    </user>
    <review>
    <xsl:value-of select="following-sibling::tr[position()=1]/td/table/tbody/tr/td/text()"/>
    </review>
    </item>
    </xsl:template>
    </xsl:stylesheet>"""


ur_with_author = """\
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
    <xsl:template match="/">
    <ur>
    <xsl:apply-templates select="//*[@class='textsm']/table[position()=2]/tbody/tr/td[position()=2]/table[position()=3]/tbody/tr[position()>=2 and ((position()-2) mod 3)=0 and count(.//*/@href)>0 and count(./following-sibling::tr[position()=1]/td/table/tbody/tr/td/text())>0]" mode="ur"/>
    </ur>
    </xsl:template>


    <xsl:template match="//*[@class='textsm']/table[position()=2]/tbody/tr/td[position()=2]/table[position()=3]/tbody/tr[position()>=2 and ((position()-2) mod 3)=0 and count(.//*/@href)>0 and count(./following-sibling::tr[position()=1]/td/table/tbody/tr/td/text())>0]" mode="ur">
    <item>
    <user>
    <xsl:value-of select="*//*/@href"/>
    <xsl:value-of select="*/@href"/>
    </user>
    <review>
    <xsl:value-of select="following-sibling::tr[position()=1]/td/table/tbody/tr/td/text()"/>
    </review>
    </item>
    </xsl:template>
    </xsl:stylesheet>"""