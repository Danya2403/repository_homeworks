# (1 способ)
# import re
# urls=re.findall(r'http(?:s)?://\S+', open('file.xml').read())
# print(urls)

# (2 способ)
# with open('file.xml','r',encoding='utf-8') as file:
#  lines=file.readlines()
# count_link=0
# for line in lines:
#  if 'http' in line:
#    end_link=0
#    while line.find(_sub:'http', end_link)!=-1:
#        start_link=line.find(_sub:'http',end_link)
#        if line[start_limk - 1]=='"':
#          end_limk=line.(_sub:'"', start_link)
#  elif line[start_link- 1]==' ':
#      end_link=line.find(_sub:' ',start_link)
#  else:
#      end_link=line.rfind('<')
#  count_link+=1
#  print(line[start_link:end_link])
# print('Колличество ссылок',count_link)
