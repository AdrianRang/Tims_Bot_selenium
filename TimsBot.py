import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

#//////////////////7/////////////////////////////////////////#

day_of_visit = int(input("Day of visit: "))
month_of_visit = int(input("Month of visit: "))
if month_of_visit < 1 or month_of_visit > 12:
    print("Error: Invalid month")
    exit()
if month_of_visit < time.localtime().tm_mon - 1 or month_of_visit > time.localtime().tm_mon and month_of_visit != 1:
    print("Error: Invalid month, tim hortons only takes surveys for the current month and the previous month")
    exit()
first_day_of_month = (datetime.date(time.localtime().tm_year, month_of_visit, 1).weekday() + 1) % 7

time_of_visit_hour = int(input("Hour of visit: "))
time_of_visit_minute = int(input("Minute of visit: "))
time_of_visit_ampm = input("AM or PM: ")


answers = [
    "Excelente sabor y presentación.",
    "Bastante satisfactoria en términos de calidad.",
    "Muy deliciosa, pero la presentación podría mejorar.",
    "Sorprendentemente deliciosa y bien presentada.",
    "Buena relación calidad-precio en general.",
    "Fresca y sabrosa.",
    "Cumplió mis expectativas en términos de calidad.",
    "Increíblemente deliciosa, pero algo grasosa.",
    "Balance perfecto entre sabor y presentación.",
    "Ligeramente insípida y decepcionante.",
    "Textura y sabor mejorables, pero decente.",
    "Sabores auténticos y muy satisfactorios.",
    "Demasiado condimentada para mi gusto.",
    "Frescura y sabor se podrían mejorar.",
    "Sabor casero y reconfortante, pero algo simple.",
    "Ingredientes de alta calidad y muy frescos.",
    "Un tanto sobrecocida, pero buen sabor en general.",
    "Calidad gourmet que justifica el precio."
]


restaurant_number_css = ".QR-QID128-1"
date_of_visit_css = ".QR-QID128-2"
calendar_css = ".ui-datepicker-calendar"
prev_month_css = ".ui-datepicker-prev"
# day_of_visit_XPATH = "/html/body/div[4]/table/tbody/tr[" + str(int(day_of_visit + ((first_day_of_month + 1) if first_day_of_month != 0 else 0 / 7) + 2))+ "]/td[" + str((day_of_visit + (first_day_of_month + 1) if first_day_of_month != 0 else 0) % 7) + "]"
row = int((day_of_visit + first_day_of_month) / 7) + 1
collumn = (day_of_visit + first_day_of_month) % 7
day_of_visit_XPATH = "/html/body/div[4]/table/tbody/tr[" + str(row) + "]/td[" + str(collumn) + "]"
print(day_of_visit_XPATH)
time_of_visit_hour_css = "#QR\~QID130\#1\~1"
time_of_visit_hour_selection_css = "#QR\~QID130\#1\~1\~" + str(time_of_visit_hour)
time_of_visit_minute_css = "#QR\~QID130\#2\~1"
time_of_visit_minute_selection_css = "#QR\~QID130\#2\~1\~" + str(time_of_visit_minute + 1)
time_of_visit_ampm_css = "#QR\~QID130\#3\~1"
time_of_visit_ampm_selection_css = "#QR\~QID130\#3\~1\~" + str(1 if time_of_visit_ampm.upper() == "AM" else 2)

next_button_css = "#NextButton"

q1_answer_css = "td.LabelContainer:nth-child(1)" # muy satisfecho
q2_answer_css = "#QR\~QID45" # pregunta abierta
q3_answer_css = "#QID18-5-label" # # comio en el restaurante
q4_answer_css = "#QID19-5-label" # En el mostrador con un miembro del equipo
q5_a_answer_css = "#QID20-5-label" # solo bebida # b es opcional
q6_answer_css = "tr.ChoiceRow:nth-child({}) > td:nth-child(2)"  # muy satisfehco
q7_answer_css = "tr.ChoiceRow:nth-child({}) > td:nth-child(2)" # altamente probable
q8_answer_css = "li.Selection:nth-child(2) > span:nth-child(3)" # no
q9_answer_css = "li.Selection:nth-child(2) > span:nth-child(3)" # Bebida fria
q10_answer_css = "tr.alt:nth-child(2) > td:nth-child(4)" # frappe oreo
q11_answer_css = "td.LabelContainer:nth-child(1)" # muy satisfecho
q12_answer_css = "tr.ChoiceRow:nth-child({}) > td:nth-child(2)" # muy satisfecho
q13_answer_css = "tr.ChoiceRow:nth-child({}) > td:nth-child(2)" # muy satisfecho
q14_answer_css = "td.LabelContainer:nth-child(1)" # muy probable
q15_answer_css = "#QR\~QID75" # pregunta abierta
q16_answer_css = "#QR\~QID76" # pregunta abierta
q17_answer_css = "li.Selection:nth-child(2) > span:nth-child(3)" # 2 veces
q18_answer_css = "li.Selection:nth-child(2) > span:nth-child(3)" # Hombre
q19_answer_css = "li.Selection:nth-child(1) > span:nth-child(3)" # menos de 18
q20_answer_css = "li.Selection:nth-child(2) > span:nth-child(3)" # No

#//////////////////7/////////////////////////////////////////#

driver = webdriver.Firefox()

try:
    driver.get("https://rbixm.qualtrics.com/jfe/form/SV_cAc1Ib5B7V4nVLE?CountryCode=MEX&Q_Language=ES&SC=Simple")
except:
    print("Error: Unable to connect to Qualtrics")
    driver.close()
    exit()

#//////////////////7/////////////////////////////////////////#

def next():
    try:
        next_button_field = driver.find_element(By.CSS_SELECTOR, next_button_css)
    except:
        print("Error: next button id invalid")
        driver.close()
        exit()
    next_button_field.click()

#//////////////////7/////////////////////////////////////////#

def wait_for_load(element):
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR, element)
            break
        except:
            pass

#//////////////////7/////////////////////////////////////////#

# wait_for_load()
time.sleep(2)
while True:
    try:
        restaurant_number_field = driver.find_element(By.CSS_SELECTOR, restaurant_number_css)
        break
    except:
        print("Error: restaurant number id invalid")
restaurant_number_field.send_keys("821107")


try:
    date_of_visit_field = driver.find_element(By.CSS_SELECTOR, date_of_visit_css)
except:
    print("Error: date of visit id invalid")
    driver.close()
    exit()
date_of_visit_field.click()


try:
    calendar_field = driver.find_element(By.CSS_SELECTOR, calendar_css)
except:
    print("Error: calendar id invalid")
    driver.close()
    exit()

if month_of_visit != time.localtime().tm_mon:
    try:
        prev_month_field = driver.find_element(By.CSS_SELECTOR, prev_month_css)
    except:
        print("Error: prev month id invalid")
        driver.close()
        exit()
    prev_month_field.click()

try:
    day_of_visit_field = driver.find_element(By.XPATH, day_of_visit_XPATH)
except:
    print("Error: day of visit xpath invalid")
    driver.close()
    exit()
day_of_visit_field.click()

while True:
    try:
        time_of_visit_hour_field = driver.find_element(By.CSS_SELECTOR, time_of_visit_hour_css)
        time_of_visit_hour_field.click()
        break
    except:
        print("Error: time of visit hour id invalid")


try:
    time_of_visit_hour_selection_field = driver.find_element(By.CSS_SELECTOR, time_of_visit_hour_selection_css)
except:
    print("Error: time of visit hour selection id invalid")
    driver.close()
    exit()
time_of_visit_hour_selection_field.click()

try:
    time_of_visit_minute_field = driver.find_element(By.CSS_SELECTOR, time_of_visit_minute_css)
except:
    print("Error: time of visit minute id invalid")
    driver.close()
    exit()
time_of_visit_minute_field.click()

try:
    time_of_visit_minute_selection_field = driver.find_element(By.CSS_SELECTOR, time_of_visit_minute_selection_css)
except:
    print("Error: time of visit minute selection id invalid")
    driver.close()
    exit()
time_of_visit_minute_selection_field.click()

try:
    time_of_visit_ampm_field = driver.find_element(By.CSS_SELECTOR, time_of_visit_ampm_css)
except:
    print("Error: time of visit am or pm id invalid")
    driver.close()
    exit()
time_of_visit_ampm_field.click()

try:
    time_of_visit_ampm_selection_field = driver.find_element(By.CSS_SELECTOR, time_of_visit_ampm_selection_css)
except:
    print("Error: time of visit am or pm selection id invalid")
    driver.close()
    exit()
time_of_visit_ampm_selection_field.click()

next()

time.sleep(2)

next()

while True:
    try:
        q1_answer_field = driver.find_element(By.CSS_SELECTOR, q1_answer_css)
        break
    except:
        print("Error: q1 answer id invalid")
q1_answer_field.click()

next()

while True:
    try:
        q2_answer_field = driver.find_element(By.CSS_SELECTOR, q2_answer_css)
        break
    except:
        print("Error: q2 answer id invalid")
q2_answer_field.send_keys(answers[random.randint(0, len(answers) - 1)])

next()

while True:
    try:
        q3_answer_field = driver.find_element(By.CSS_SELECTOR, q3_answer_css)
        break
    except:
        print("Error: q3 answer id invalid")
q3_answer_field.click()

next()

while True:
    try:
        q4_answer_field = driver.find_element(By.CSS_SELECTOR, q4_answer_css)
        break
    except:
        print("Error: q4 answer id invalid")
q4_answer_field.click()

next()

while True:
    try:
        q5_a_answer_field = driver.find_element(By.CSS_SELECTOR, q5_a_answer_css)
        break
    except:
        print("Error: q5 a answer id invalid")
q5_a_answer_field.click()

next()

while True:
    try:
        driver.find_element(By.CSS_SELECTOR, q6_answer_css.format("1"))
        break
    except:
        print("Error: q5 b answer id invalid")

for i in range(1, 10):
    try:
        q6_answer_field = driver.find_element(By.CSS_SELECTOR, q6_answer_css.format(i))
    except:
        print("Error: q6 answer id {} invalid".format(q6_answer_css.format(str(i))))
        driver.close()
        exit()
    q6_answer_field.click()

next()

time.sleep(1)

next()

while True:
    try:
        q7_a_answer_field = driver.find_element(By.CSS_SELECTOR, q7_answer_css.format("1"))
        break
    except:
        print("Error: q7 a answer id invalid")

try:
    q7_b_answer_field = driver.find_element(By.CSS_SELECTOR, q7_answer_css.format("2"))
except:
    print("Error: q7 b answer id invalid")
    driver.close()
    exit()
q7_a_answer_field.click()
q7_b_answer_field.click()

next()

while True:
    try:
        q8_answer_field = driver.find_element(By.CSS_SELECTOR, q8_answer_css)
        break
    except:
        print("Error: q8 answer id invalid")
q8_answer_field.click()

next()

time.sleep(1)

while True:
    try:
        q9_answer_field = driver.find_element(By.CSS_SELECTOR, q9_answer_css)
        break
    except:
        print("Error: q9 answer id invalid")
q9_answer_field.click()

next()

wait_for_load(q10_answer_css)

# while True:
try:
    q10_answer_field = driver.find_element(By.CSS_SELECTOR, q10_answer_css)
    # break
except:
    print("Error: q10 answer id invalid")
q10_answer_field.click()

next()

while True:
    try:
        q11_answer_field = driver.find_element(By.CSS_SELECTOR, q11_answer_css)
        break
    except:
        print("Error: q11 answer id invalid")
q11_answer_field.click()

next()

for i in range(1, 4):
    while True:
        try:
            q12_answer_field = driver.find_element(By.CSS_SELECTOR, q12_answer_css.format(i))
            break
        except:
            print("Error: q12 {} answer id invalid".format(q12_answer_css.format(str(i))))
    q12_answer_field.click()

next()

time.sleep(1)

for i in range(1, 6):
    while True:
        try:
            q13_answer_field = driver.find_element(By.CSS_SELECTOR, q13_answer_css.format(i))
            break
        except:
            print("Error: q13 {} answer id invalid".format(q13_answer_css.format(str(i))))
    q13_answer_field.click()

next()

while True:
    try:
        q14_answer_field = driver.find_element(By.CSS_SELECTOR, q14_answer_css)
        break
    except:
        print("Error: q14 answer id invalid")
q14_answer_field.click()

next()

while True:
    try:
        q15_answer_field = driver.find_element(By.CSS_SELECTOR, q15_answer_css)
        break
    except:
        print("Error: q15 answer id invalid")
q15_answer_field.send_keys(answers[random.randint(0, len(answers) - 1)])

next()

while True:
    try:
        q16_answer_field = driver.find_element(By.CSS_SELECTOR, q16_answer_css)
        break
    except:
        print("Error: q16 answer id invalid")
q16_answer_field.send_keys("no")

next()

while True:
    try:
        q17_answer_field = driver.find_element(By.CSS_SELECTOR, q17_answer_css)
        break
    except:
        print("Error: q17 answer id invalid")
q17_answer_field.click()

next()

time.sleep(1)

next()

wait_for_load(q18_answer_css)

try:
    q18_answer_field = driver.find_element(By.CSS_SELECTOR, q18_answer_css)
except:
    print("Error: q18 answer id invalid")
    driver.close()
    exit()
q18_answer_field.click()

next()

time.sleep(0.5)

wait_for_load(q19_answer_css)

try:
    q19_answer_field = driver.find_element(By.CSS_SELECTOR, q19_answer_css)
except:
    print("Error: q19 answer id invalid")
    driver.close()
    exit()
q19_answer_field.click()

next()

while True:
    try:
        q20_answer_field = driver.find_element(By.CSS_SELECTOR, q20_answer_css)
        q20_answer_field.click()
        break
    except:
        print("Error: q20 answer id invalid")

next()