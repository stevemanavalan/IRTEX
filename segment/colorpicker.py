# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:45:56 2020

@author: steve
"""

class colorpicker:
    def name2hue(self,colorname):
        pink = ["#FFC0CB","#FFB6C1","#FF69B4","#FF1493","#D87093","#C71585"]
        purple = ["#E6E6FA","#D8BFD8","#DDA0DD","#DA70D6","#EE82EE","#FF00FF","#FF00FF","#BA55D3","#9932CC","#9400D3","#8A2BE2","#8B008B","#800080","#9370DB","#7B68EE","#6A5ACD","#483D8B","#663399","#4B0082"]
        red = ["#FFA07A","#FA8072","#E9967A","#F08080","#CD5C5C","#DC143C","#FF0000","#B22222","#8B0000"]
        orange = [ "#FFA500","#FF8C00","#FF7F50","#FF6347","#FF4500"]
        yellow = ["#FFD700","#FFFF00","#FFFFE0","#FFFACD","#FAFAD2","#FFEFD5","#FFE4B5","#FFDAB9","#EEE8AA","#F0E68C","#BDB76B"]  
        green = ["#ADFF2F","#7FFF00","#7CFC00","#00FF00","#32CD32","#98FB98","#90EE90","#00FA9A","#00FF7F","#3CB371","#2E8B57","#228B22","#008000","#006400","#9ACD32","#6B8E23","#556B2F","#66CDAA","#8FBC8F","#20B2AA","#008B8B","#008080"]
        cyan = ["#00FFFF","#00FFFF","#E0FFFF","#AFEEEE","#7FFFD4","#40E0D0","#48D1CC","#00CED1"]        
        blue = ["#5F9EA0","#4682B4","#B0C4DE","#ADD8E6","#B0E0E6","#87CEFA","#87CEEB","#6495ED","#00BFFF","#1E90FF","#4169E1","#0000FF","#0000CD","#00008B","#000080","#191970"]
        brown = ["#FFF8DC","#FFEBCD","#FFE4C4","#FFDEAD","#F5DEB3","#DEB887","#D2B48C","#BC8F8F","#F4A460","#DAA520","#B8860B","#CD853F","#D2691E","#808000","#8B4513","#A0522D","#A52A2A","#800000"]       
        white = ["#FFFFFF","#FFFAFA","#F0FFF0","#F5FFFA","#F0FFFF","#F0F8FF","#F8F8FF","#F5F5F5","#FFF5EE","#F5F5DC","#FDF5E6","#FFFAF0","#FFFFF0","#FAEBD7","#FAF0E6","#FFF0F5","#FFE4E1"]                       
        grey = [ "#DCDCDC","#D3D3D3","#C0C0C0","#A9A9A9","#696969","#808080","#778899","#708090","#2F4F4F","#000000"]        
        if any(colorname in s for s in pink):
            return "pink"
        if any(colorname in s for s in purple):
            return "purple"
        if any(colorname in s for s in red):
            return "red"
        if any(colorname in s for s in orange):
            return "orange"
        if any(colorname in s for s in yellow):
            return "yellow"
        if any(colorname in s for s in green):
            return "green"
        if any(colorname in s for s in cyan):
            return "cyan"
        if any(colorname in s for s in blue):
            return "blue"
        if any(colorname in s for s in brown):
            return "brown"
        if any(colorname in s for s in white):
            return "white"
        if any(colorname in s for s in grey):
            return "grey"
        
        
        