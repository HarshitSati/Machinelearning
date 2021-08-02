from fpdf import FPDF
from datetime import date
import time
from helper import get_state_names, get_country_names, Mode
from daily_counts import plot_daily_count_states, plot_daily_count_countries
from time_series_analysis import plot_states, plot_countries


WIDTH = 210
HEIGHT = 297

def create_title(day,time,  pdf):

    pdf.set_font('Arial', '', 24)
    pdf.ln(40)
    pdf.cell(0, 10, 'Covid Analytics Report', align = 'C')
#    pdf.write(5, f"Covid Analytics Report")
    pdf.ln(15)
    pdf.set_text_color(	128, 128, 128)
    pdf.set_font('Arial', '', 12)
    pdf.write(4, f'Day: {day}')
    pdf.ln(5)
    pdf.set_font('Arial', '', 12)
    pdf.write(4, f'Time: {time}')


def create_report(day, time,  filename):
    """ 3 args: day which accepts the current date
              filename which logs the name of the file
    """

    #pdf.cell(40, 10, 'Hello World!')
    pdf = FPDF()
    """ First Page """
    pdf.add_page()
    pdf.image("./generate-analytics-report/resources/header_IND.jpg", 0, 0 , WIDTH)
    create_title(day,time, pdf) # creates a title for the pdf
    #pdf.add_page()
    states = ["New Hampshire", "Massachusetts"]
    plot_daily_count_states(states, filename = "1.png")
    pdf.image("1.png", 5, 100, WIDTH/2-5)

    plot_daily_count_states(states, mode= Mode.DEATHS, filename = "2.png")
    pdf.image("2.png", WIDTH/2 +5, 100, WIDTH/2-5)

    #""" Second Page """
    #pdf.add_page()
    plot_states(states, days = 7, filename = "3.png", end_date = day)
    pdf.image("3.png", 5, 175, WIDTH/2-5)

    plot_states(states,days = 7, mode= Mode.DEATHS, filename = "4.png",end_date = day)
    pdf.image("4.png", WIDTH/2 +5, 175, WIDTH/2-5)

    """ Footer """
    pdf.image("./generate-analytics-report/footer.png",  0, HEIGHT- 21 , WIDTH)
    pdf.output(filename)

if __name__ == '__main__':
    day = date.today().strftime("%m/%d/%y").lstrip('0')
    t = time.strftime("%H:%M:%S").lstrip('0') #note to self :to check for trailing 0
    create_report(day,t, "report.pdf")
