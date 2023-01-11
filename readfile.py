import re


class Read:

    def __init__(self, input_text, output_text):

        self.input_text = input_text
        self.output_text = output_text

    def Modify_MGO(self):
        file_read = open(self.input_text, 'r')
        lines = file_read.readlines()
        for line in lines:
            words = line.split()
            month = words[0]
            date = words[1]
            time = words[2]
            loglevel = words[3]
            location = words[4]
            description = ' '.join(words[5:])
            mod_desc = description.replace(",", " ")
            final = f"{month},{date},{time},{loglevel},{location},{mod_desc} \n"
            content = open(self.output_text, "a")
            modified_file = content.write(final)
            if len(final) != 0:
                continue
            file_read.close()
            return modified_file

    def Modify_cloud(self):
        file_read = open(self.input_text, 'r')
        lines = file_read.readlines()
        for line in lines:
            words = line.split()
            date = words[0]
            time = words[1]
            loglevel = words[3]
            location = words[4]
            req_id = '  '.join(words[5:11])
            description = ' '.join(words[11:]).replace(",", " ")
            final = f"{date},{time},{loglevel},{location},{req_id},{description} \n"
            content = open(self.output_text, "a")
            modified_file = content.write(final)
            if len(final) != 0:
                continue
            file_read.close()
            return modified_file

    def Modify_OBSFAILA(self):
        file_read = open(self.input_text, 'r')
        lines = file_read.readlines()
        text0 = "REPORT NUMBER       :"
        text1 = "CALL ID"
        text2 = "CALL START"
        text3 = "CLEAR CODE :"
        text4 = "CLEAR INFO :"
        text5 = "CLEAR PART :"
        text6 = "SIGNALLING :"
        text7 = "CALLING NUMBER      :"
        text8 = "CALLED NUMBER"
        text9 = "IMSI              :"
        text10 = "CGR/BSC/PCM-TSL"
        text11 = "LAC/CI/CELL BAND  :"
        new_list0 = []
        new_list1 = []
        new_list2 = []
        new_list3 = []
        new_list4 = []
        new_list5 = []
        new_list6 = []
        new_list7 = []
        new_list8 = []
        new_list9 = []
        new_list10 = []
        new_list11 = []
        idx = 0
        for line in lines:
            if text0 in line:
                new_list0.insert(idx, line)
            if text1 in line:
                new_list1.insert(idx, line)
            if text2 in line:
                new_list2.insert(idx, line)
            if text3 in line:
                new_list3.insert(idx, line)
            if text4 in line:
                new_list4.insert(idx, line)
            if text5 in line:
                new_list5.insert(idx, line)
            if text6 in line:
                new_list6.insert(idx, line)
            if text7 in line:
                new_list7.insert(idx, line)
            if text8 in line:
                new_list8.insert(idx, line)
            if text9 in line:
                new_list9.insert(idx, line)
            if text10 in line:
                new_list10.insert(idx, line)
            if text11 in line:
                new_list11.insert(idx, line)
                idx += 1
        linelen = len(new_list0)
        for i in range(linelen):
            t0 = new_list0[i].strip('\n''REPORT NUMBER       :')
            t1 = new_list1[i].strip('\n''CALL ID             :')
            t2 = new_list2[i].strip('\n''CALL START          :''CALL PHASE : RELEASE''CALL PHASE : INTERRUPT')
            t3 = new_list3[i].strip('\n')
            t4 = new_list4[i].strip('\n')
            t5 = new_list5[i].strip('\n')
            t6 = new_list6[i].strip('\n')
            t7 = new_list7[i].strip('\n''CALLING NUMBER      :')
            t_8 = new_list8[i].strip('\n''CALLED NUMBER')
            t8 = re.sub("[: N|I]", " ", t_8)
            t9 = new_list9[i].strip('\n')
            t10 = new_list10[i].strip('\n')
            t11 = new_list11[i].strip('\n')
            matches3 = (re.compile(r"\w{4}H")).findall(t3)
            matches4 = (re.compile(r"\w{6}\s\w{5}\s\w{5}")).findall(t4)
            matches5 = (re.compile(r"\w+\s?\w+$")).findall(t5)
            matches6 = (re.compile(r"[\w-]+\s*\w*$")).findall(t6)
            for t6p in matches6:
                for t5p in matches5:
                    for t4p in matches4:
                        for t3p in matches3:
                            final = f"{t0},{t1},{t2},{t3p},{t4p},{t5p},{t6p},{t7}," \
                                    f"{t8},{t9[22:37]},{t9[48:63]},{t10[22:37]},{t10[48:63]}," \
                                    f"{t11[22:37]},{t11[48:63]}\n"
                            content = open(self.output_text, "a")
                            modified_file = content.write(final)
                            if len(t0) != 0:
                                continue
                            file_read.close()
                            return modified_file
       
