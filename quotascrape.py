#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import ttk
from tkinter import *
import re


# In[13]:


'''
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver1 = webdriver.Chrome(options=options)
driver1.get("https://registration.boun.edu.tr/buis/General/schedule.aspx?p=semester")

wait = WebDriverWait(driver1, 10)
element1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="submit"]')))
element_id1 = element1.get_attribute('id')
go_button = wait.until(EC.presence_of_element_located((By.ID, element_id1)))


go_button.click()

driver1.implicitly_wait(3)

link_elements = driver1.find_elements(By.TAG_NAME, 'a')

urls = []

for link in link_elements:
    urls.append(link.get_attribute('href'))

driver1.quit()
'''


# In[14]:


options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url_dict = {
    'DSAI': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=DSAI&bolum=ARTIFICIAL+INTELLIGENCE',
    'ASIA': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ASIA&bolum=ASIAN+STUDIES',
    'ASIL': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ASIA&bolum=ASIAN+STUDIES',
    'ATA': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ATA&bolum=ATATURK+INSTITUTE+FOR+MODERN+TURKISH+HISTORY',
    'HTR': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ATA&bolum=ATATURK+INSTITUTE+FOR+MODERN+TURKISH+HISTORY',
    'AUTO': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=AUTO&bolum=AUTOMOTIVE+ENGINEERING',
    'BM': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=BM&bolum=BIOMEDICAL+ENGINEERING',
    'BIS': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=BIS&bolum=BUSINESS+INFORMATION+SYSTEMS',
    'CHE': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CHE&bolum=CHEMICAL+ENGINEERING',
    'CHEM': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CHEM&bolum=CHEMISTRY',
    'STS': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CHEM&bolum=CHEMISTRY',
    'CE': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CE&bolum=CIVIL+ENGINEERING',
    'ENGG': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CE&bolum=CIVIL+ENGINEERING',
    'COGS': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=COGS&bolum=COGNITIVE+SCIENCE',
    'CSE': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CSE&bolum=COMPUTATIONAL+SCIENCE+%26+ENGINEERING',
    'CET': ['https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CET&bolum=COMPUTER+EDUCATION+%26+EDUCATIONAL+TECHNOLOGY', "https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CET&bolum=EDUCATIONAL+TECHNOLOGY"],
    'CMPE': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CMPE&bolum=COMPUTER+ENGINEERING',
    'CEM': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CEM&bolum=CONSTRUCTION+ENGINEERING+AND+MANAGEMENT',
    'CCS': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=CCS&bolum=CRITICAL+AND+CULTURAL+STUDIES',
    'PRED': ['https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=PRED&bolum=EARLY+CHILDHOOD+EDUCATION',"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=PRSO&bolum=UNDERGRADUATE+PROGRAM+IN+PRESCHOOL+EDUCATION"],
    'EQE': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=EQE&bolum=EARTHQUAKE+ENGINEERING',
    'EC': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=EC&bolum=ECONOMICS',
    'ED': ["https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ED&bolum=EDUCATIONAL+SCIENCES","https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=GUID&bolum=GUIDANCE+%26+PSYCHOLOGICAL+COUNSELING" ],
    'EE': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=EE&bolum=ELECTRICAL+%26+ELECTRONICS+ENGINEERING',
    'ETM': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ETM&bolum=ENGINEERING+AND+TECHNOLOGY+MANAGEMENT',
    'ESC': ['https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ENV&bolum=ENVIRONMENTAL+SCIENCES',"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ENVT&bolum=ENVIRONMENTAL+TECHNOLOGY"],
    'ADEX': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=XMBA&bolum=EXECUTIVE+MBA',
    'PA': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=PA&bolum=FINE+ARTS',
    'FLED': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=FLED&bolum=FOREIGN+LANGUAGE+EDUCATION',
    'GED': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=GED&bolum=GEODESY',
    'GPH': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=GPH&bolum=GEOPHYSICS',
    'GR': '',
    'HIST': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=HIST&bolum=HISTORY',
    'LAT': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=HIST&bolum=HISTORY',
    'HUM': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=HUM&bolum=HUMANITIES+COURSES+COORDINATOR',
    'IE': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=IE&bolum=INDUSTRIAL+ENGINEERING',
    'INCT': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=INCT&bolum=INTERNATIONAL+COMPETITION+AND+TRADE',
    'INTT': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=INTT&bolum=INTERNATIONAL+TRADE',
    'LAW': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LAW&bolum=LAW+PR.',
    'LS': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LS&bolum=LEARNING+SCIENCES',
    'CAU': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LING&bolum=LINGUISTICS',
    'LING': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LING&bolum=LINGUISTICS',
    'TID': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LING&bolum=LINGUISTICS',
    'AD': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=AD&bolum=MANAGEMENT',
    'MIS': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=MIS&bolum=MANAGEMENT+INFORMATION+SYSTEMS',
    'MATH': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=MATH&bolum=MATHEMATICS',
    'SCED': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=SCED&bolum=MATHEMATICS+AND+SCIENCE+EDUCATION',
    'ME': 'https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=ME&bolum=MECHANICAL+ENGINEERING',
    'MECA': ["https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=MECA&bolum=MECHATRONICS+ENGINEERING+(WITH+THESIS)","https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=MECA&bolum=MECHATRONICS+ENGINEERING+(WITH+THESIS)"],
    "BIO":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=BIO&bolum=MOLECULAR+BIOLOGY+%26+GENETICS",
    "PHIL":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=PHIL&bolum=PHILOSOPHY",
    "PE":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=PE&bolum=PHYSICAL+EDUCATION",
    "PHYL":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=PHYS&bolum=PHYSICS",
    "PHYS":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=PHYS&bolum=PHYSICS",
    "POLS":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=POLS&bolum=POLITICAL+SCIENCE%26INTERNATIONAL+RELATIONS",
    "PSY":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=PSY&bolum=PSYCHOLOGY",
    "AE":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "ARM":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "CHIN":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "FR":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "GER":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "ITA":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "JP":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "KR":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "POR":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "RUS":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "SPA":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=YADYOK&bolum=SCHOOL+OF+FOREIGN+LANGUAGES",
    "SPL":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=SPL&bolum=SOCIAL+POLICY+WITH+THESIS",
    "KRD":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=SOC&bolum=SOCIOLOGY",
    "SOC":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=SOC&bolum=SOCIOLOGY",
    "SWE":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=SWE&bolum=SOFTWARE+ENGINEERING",
    "TRM":["https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TRM&bolum=SUSTAINABLE+TOURISM+MANAGEMENT","https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TRM&bolum=TOURISM+ADMINISTRATION"],
    "SCO":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=SCO&bolum=SYSTEMS+%26+CONTROL+ENGINEERING",
    "TR":["https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=WTR&bolum=TRANSLATION","https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TR&bolum=TRANSLATION+AND+INTERPRETING+STUDIES"],
    "INT":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TR&bolum=TRANSLATION+AND+INTERPRETING+STUDIES",
    "TK":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TK&bolum=TURKISH+COURSES+COORDINATOR",
    "AR":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TKL&bolum=TURKISH+LANGUAGE+%26+LITERATURE",
    "PER":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TKL&bolum=TURKISH+LANGUAGE+%26+LITERATURE",
    "TKF":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TKL&bolum=TURKISH+LANGUAGE+%26+LITERATURE",
    "TKL":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=TKL&bolum=TURKISH+LANGUAGE+%26+LITERATURE",
    "AL":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES",
    "AS":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES",
    "CL":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES",
    "DRA":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES",
    "EL":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES",
    "ENGL":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES",
    "FA":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES",
    "LIT":"https://registration.boun.edu.tr/scripts/sch.asp?donem=2022/2023-2&kisaadi=LL&bolum=WESTERN+LANGUAGES+%26+LITERATURES",
}

def get_data(selected_url):
    dfs = []

    
    driver.get(url_dict[selected_url])
    info_links = driver.find_elements(By.LINK_TEXT,"Info")
    for info_link in info_links:
        info_link.click()
        # Switch to the new window
        new_window = driver.window_handles[-1]
        driver.switch_to.window(new_window)
        try:
            # Find the table element
            table = driver.find_element(By.TAG_NAME, "table")
            # Convert the table content to a DataFrame
            df2 = pd.read_html(table.get_attribute('outerHTML'))[0]
            strongs = driver.find_elements(By.TAG_NAME, "strong")
            strongs_text = [strong.text for strong in strongs]
            strongs_text_repeated = np.repeat(strongs_text, len(df2))
            df2["Code"] = strongs_text_repeated[:len(df2)]
            dfs.append(df2)
        except IndexError:
            # No table found, move on to the next link
            pass
        finally:
            # Close the new window
            driver.close()
            # Switch back to the main window
            main_window = driver.window_handles[0]
            driver.switch_to.window(main_window)


    result = pd.concat(dfs, ignore_index=True)
    result = result[["Code",0,1,2,3,4]]
    result.drop(result.columns[[5]], axis=1, inplace=True)
    result.columns = ['Code', 'Department', 'Status', 'Quota', 'Current Quota']

    words = ["Departmental Quotas:", "Department", "OZELLISANS", "PHD","MASTER","OZELMASTER","OZELPHD"]

    result = result[result.Department.isin(words) == False]
    result = result[result.Status.isin(words) == False]
    result['Code'] = result['Code'].str.replace(r'([A-Za-z]+)(\d)', r'\1 \2')
    result = result[result.Code.str.extract('(\d)').astype(int).isin([5,6,7]).any(axis=1) == False]
    
    result.reset_index(drop=True, inplace=True)

    def get_availability(row):
        quota = row['Quota']
        try:
            quota = int(quota)
        except ValueError:
            pass
        current_quota = int(row['Current Quota'])

            
        if isinstance(quota, int) and current_quota == quota:
            return "Full"
        elif isinstance(quota, int) and current_quota < quota:
            return "Available"
        elif isinstance(quota, int) and current_quota > quota:
            return "Try to get consent"
        elif isinstance(quota, str):
            return "Available"       
    
    result["Availability"] = result.apply(get_availability, axis=1)
    return result




# In[15]:


# testingdata = get_data("HTR")
# testingdata


# In[25]:


rowdata = pd.read_csv("data1.csv")
# testingdata = pd.read_csv("data1.csv") # for testing

# testingdata = get_data() IF YOU WANT TO GET ALL THE DATA

def update_table(code_filter='', availability_filter='', grade_filter='', search_filter="" ):
    # filtered_data = testingdata.copy() # IF YOU WANT TO USE ALL THE DATA
    filtered_data = get_data(code_filter_var.get()) 
    if code_filter:
        filtered_data = filtered_data[filtered_data['Code'].str.contains(code_filter)]
    if availability_filter:
        filtered_data = filtered_data[filtered_data['Availability'] == availability_filter]
    if grade_filter:
        grade = int(grade_filter)
        filtered_data = filtered_data[filtered_data['Code'].str.contains(fr'\b{grade}\d{{2}}\b')]
    if search_filter:
        search_filter = search_filter.lower().replace(' ', '')
        filtered_data = filtered_data[filtered_data['Code'].str.lower().str.contains(search_filter)]
            
    table.delete(*table.get_children())  # clear the table
    for i, row in filtered_data.iterrows():
        table.insert('', 'end', values=row.tolist(), iid=i)


root = tk.Tk()
root.title("Course Availability")
root.iconbitmap('G:\My Drive\Collab\Python\PythonProjects\QuotaTracker\Boğaziçi_Üniversitesi_Logo.ico')


table_frame = ttk.Frame(root)
table_frame.pack(padx=10, pady=10)

table = ttk.Treeview(table_frame, columns=['Code', 'Department', 'Status', 'Quota', 'Current Quota', 'Availability'])
table.heading('#0', text='Index')
table.heading('Code', text='Code')
table.heading('Department', text='Department')
table.heading('Status', text='Status')
table.heading('Quota', text='Quota')
table.heading('Current Quota', text='Current Quota')
table.heading('Availability', text='Availability')
table.column('#0', width=0, stretch=tk.NO)
table.column('Code', width=120, anchor=tk.CENTER)
table.column('Department', width=100, anchor=tk.CENTER)
table.column('Status', width=100, anchor=tk.CENTER)
table.column('Quota', width=100, anchor=tk.CENTER)
table.column('Current Quota', width=120, anchor=tk.CENTER)
table.column('Availability', width=120, anchor=tk.CENTER)
table_scroll = ttk.Scrollbar(table_frame, orient='vertical', command=table.yview)
table_scroll.pack(side='right', fill='y')
table.configure(yscrollcommand=table_scroll.set)
table.pack()


code_filter_var = tk.StringVar()
code_filter_var.set('')
code_filter_label = ttk.Label(root, text='Filter by Code:')
code_filter_label.pack()
code_values = rowdata['Code'].str.extract(r'([A-Z]+)').dropna().drop_duplicates().values.squeeze().tolist()
code_values.sort()
code_filter_dropdown = ttk.Combobox(root, textvariable=code_filter_var, values=code_values + [''], state='readonly')
code_filter_dropdown.pack()

availability_filter_var = tk.StringVar()
availability_filter_var.set('')
availability_filter_label = ttk.Label(root, text='Filter by Availability:')
availability_filter_label.pack()
availability_filter_dropdown = ttk.Combobox(root, textvariable=availability_filter_var, values=['Full', 'Available', 'Try to get consent', ''], state='readonly')
availability_filter_dropdown.pack()

grade_filter_var = tk.StringVar()
grade_filter_var.set('')
grade_filter_label = ttk.Label(root, text='Filter by Grade:')
grade_filter_label.pack()
grade_filter_dropdown = ttk.Combobox(root, textvariable=grade_filter_var, values=['1', '2', '3', '4', ''], state='readonly')
grade_filter_dropdown.pack()

'''
search_filter_var = tk.StringVar()
search_filter_var.set('')   
search_filter_label = ttk.Label(root, text='Search:')
search_filter_label.pack()
search_filter_entry = ttk.Entry(root, textvariable=search_filter_var)
search_filter_entry.pack()
'''

search_button = ttk.Button(root, text="Search", command=lambda: update_table(code_filter_var.get(), availability_filter_var.get(), grade_filter_var.get()))
search_button.pack(padx=10, pady=10)


# Insert data into the table
# for i, row in testingdata.iterrows():
    # table.insert('', 'end', values=row.tolist(), iid=i)

root.mainloop()

