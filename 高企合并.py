from PyPDF2 import PdfFileMerger
import os

# f1=r"d:\1\1253－1315 技术专家-批量2021-09-08 1.pdf"
# f2=r"d:\2\1253－1315 技术专家-批量2021-09-08 2.pdf"


for i in range(1,129,2):
    f1=r"d:\1\1379~结束－技术专家-批量2021-09-08-3 {}.pdf".format(i)
    f2=r"d:\2\1379~结束－技术专家-批量2021-09-08-3 {}.pdf".format(i+1)
    paths =[f1,f2]
    file_merger = PdfFileMerger()
    for pdf in paths:
        #print(r"d:\s\merge{}.pdf".format(i))
        file_merger.append(pdf)
    file_merger.write(r"d:\s\13{}.pdf".format((i+1)/2 +78))
    



    #print(f1)
    #print(f2)



#paths = [r"d:\3\1253－1315 技术专家-批量2021-09-08 1.pdf", r'd:\4\1253－1315 技术专家-批量2021-09-08 2.pdf']
# merge_pdfs(paths, output='merged.pdf')
#file_merger = PdfFileMerger()
#for pdf in paths:
#    file_merger.append(pdf)
#file_merger.write(r"d:\merge.pdf")
