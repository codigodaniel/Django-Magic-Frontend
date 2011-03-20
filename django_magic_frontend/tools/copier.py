#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       copier.py
#       
#       Copyright 2011 Daniel Ceillan <daniel.ceillan@yahoo.es>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

class DjangoBaker:
    def __init__(self, original_model_name):
        self.on=original_model_name
        self.files_obvious_names=[
            '_confirm_delete.html',
            '_detail.html',
            '_form.html',
            '_list.html',
            ]
    def go(self):
		for model_name in self.new_models:
			for new_file_name in self.files_obvious_names:
				self.copy_file(self.on +new_file_name, model_name +new_file_name)
    def copy_file(self,origin_file, destiny_file):#,, dn, on
        of= open(origin_file,'r')#origin file
        df= open(destiny_file,'w')#destiny file
        l=of.readlines()
        text=''
        for i in l:
            text+=i
        df.writelines(text)
        of.close()
        df.close()

def main():
    db=DjangoBaker('label')
    db.new_models=[
    'addressbook',
    'address',
    'email',
    'telephone',
    'instantmessenger',
    'webpage',
    'domainmanager',
    'domain',
    'account',
    ]
    db.go()

if __name__ == '__main__':
    main()
