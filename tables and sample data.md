# Database tables

CREATE TABLE billionaires2023
(
    worldrank integer,
    finalworth integer,
    category text,
    personname text,
    age integer,
    country text,
    city text,
    source text,
    industries text,
    countryofcitizenship text,
    organization text,
    selfmade text,
    status text,
    gender text,
    birthdate date,
    lastname text,
    firstname text,
    title text,
    date date,
    state text,
    residencestateregion text,
    birthyear integer,
    birthmonth integer,
    birthday integer
)

# Sample Data

"worldrank"	"finalworth"	"category"	"personname"	"age"	"country"	"city"	"source"	"industries"	"countryofcitizenship"	"organization"	"selfmade"	"status"	"gender"	"birthdate"	"lastname"	"firstname"	"title"	"date"	"state"	"residencestateregion"	"birthyear"	"birthmonth"	"birthday"
1	211000	"Fashion & Retail"	"Bernard Arnault & family"	74	"France"	"Paris"	"LVMH"	"Fashion & Retail"	"France"	"LVMH Moët Hennessy Louis Vuitton"	"false"	"U"	"M"	"1949-03-05"	"Arnault"	"Bernard"	"Chairman and CEO"	"2023-04-04"			1949	3	5
2	180000	"Automotive"	"Elon Musk"	51	"United States"	"Austin"	"Tesla, SpaceX"	"Automotive"	"United States"	"Tesla"	"true"	"D"	"M"	"1971-06-28"	"Musk"	"Elon"	"CEO"	"2023-04-04"	"Texas"	"South"	1971	6	28
3	114000	"Technology"	"Jeff Bezos"	59	"United States"	"Medina"	"Amazon"	"Technology"	"United States"	"Amazon"	"true"	"D"	"M"	"1964-01-12"	"Bezos"	"Jeff"	"Chairman and Founder"	"2023-04-04"	"Washington"	"West"	1964	1	12
4	107000	"Technology"	"Larry Ellison"	78	"United States"	"Lanai"	"Oracle"	"Technology"	"United States"	"Oracle"	"true"	"U"	"M"	"1944-08-17"	"Ellison"	"Larry"	"CTO and Founder"	"2023-04-04"	"Hawaii"	"West"	1944	8	17
5	106000	"Finance & Investments"	"Warren Buffett"	92	"United States"	"Omaha"	"Berkshire Hathaway"	"Finance & Investments"	"United States"	"Berkshire Hathaway Inc. (Cl A)"	"true"	"D"	"M"	"1930-08-30"	"Buffett"	"Warren"	"CEO"	"2023-04-04"	"Nebraska"	"Midwest"	1930	8	30



CREATE TABLE user_questions
(
    user_question,
    standardised_question,
    sql_query,
    final_response,
    user_name
)

# Sample Data
"user_question"	"standardised_question"	"sql_query"	"final_response"
"Who are the top 5 self made billionaries in India?"	"Who are the top 5 self made billionaries in India?"	"SELECT personname 
FROM billionaires2023 
WHERE country = 'India' AND selfmade = 'true' 
ORDER BY finalworth DESC 
LIMIT 5"	"The top 5 self-made billionaires in India are Gautam Adani, Shiv Nadar, Dilip Shanghvi, Radhakishan Damani, and Uday Kotak." "ramkipalle"
"Who are the top 5 billionaires in the world?"	"Who are the top 5 billionaires in the world?"	"SELECT personname 
FROM billionaires2023 
ORDER BY finalworth DESC 
LIMIT 5"	"The top 5 billionaires in the world are Bernard Arnault & family, Elon Musk, Jeff Bezos, Larry Ellison, and Warren Buffett." "ramkipalle"