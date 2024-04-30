from moa import get_moa_news
from summary import summarize
from translator import translator
import datetime

# Get today's date
today_date = datetime.date.today().strftime('%Y-%m-%d')

# Create a new file with today's date as the name
file_name = today_date + '.md'

news = get_moa_news()

for new in news:
    summary = summarize(new['article'])
    summary_zh = translator(summary)
    with open(file_name, 'a') as f:
        f.write('## ' + new['title'] + '--' + new['date'] + '\n')
        f.write("**总结：**\n")
        f.write(summary_zh + '\n\n')





