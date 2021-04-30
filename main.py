from flask import Flask, render_template
import json
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def condition():

    with open("condition.json", "r", encoding='utf-8') as f:
        contents = json.loads(f.read())
    title = contents['title']
    subtitle = contents['subtitle']
    assets = contents['assets']
    coupon = contents['coupon']
    maturity_barrier1 = contents['maturity_barrier1']
    coupon_barrier = contents['coupon_barrier']
    autocall_barrier = contents['autocall_barrier']
    frequency_maturity1 = contents['frequency_maturity1']
    currency = contents['currency']
    frequency_autocall1 = contents['frequency_autocall1']
    frequency_coupon1 = contents['frequency_coupon1']
    stepdown = contents['stepdown']
    issuer_rating = contents['issuer_rating']
    cite = contents['cite']
    author = contents['author']
    facts = contents['facts']
    purposes = contents['purposes']
    title_purposes = contents['title_purposes']
    story = contents['story']




    output = render_template('condition.html',
                             title = title,
                             subtitle = subtitle,
                             coupon = coupon,
                             assets = assets,
                             maturity_barrier1 = maturity_barrier1,
                             coupon_barrier = coupon_barrier,
                             autocall_barrier = autocall_barrier,
                             frequency_maturity1 = frequency_maturity1,
                             currency = currency,
                             frequency_autocall1 = frequency_autocall1,
                             frequency_coupon1 = frequency_coupon1,
                             stepdown = stepdown,
                             issuer_rating = issuer_rating,
                             cite = cite,
                             author = author,
                             facts = facts,
                             purposes = purposes,
                             title_purposes = title_purposes,
                             story = story
                             )
    return output

@app.route('/description')
def description():

    with open("data.json", "r", encoding='utf-8') as f:
        contents = json.loads(f.read())
    name = contents.keys()
    description = []
    marcap = []
    sales_growth = []
    ebitda_margin = []
    eps_growth = []
    net_debt_ebitda = []
    target = []
    short_name = []
    full_description = []

    for i in contents.values():
        description.append(i['description'])
        marcap.append(i['marcap'])
        sales_growth.append(i['sales_growth'])
        ebitda_margin.append(i['ebitda_margin'])
        eps_growth.append(i['eps_growth'])
        net_debt_ebitda.append(i['net_debt_ebitda'])
        target.append(i['target'])
        short_name.append(i['short_name'])
        full_description.append(i['full_description'])

    output = render_template('description.html',
                             name = name,
                             description = description,
                             marcap = marcap,
                             sales_growth = sales_growth,
                             ebitda_margin = ebitda_margin,
                             eps_growth = eps_growth,
                             net_debt_ebitda = net_debt_ebitda,
                             target = target,
                             short_name = short_name,
                             full_description = full_description)

    return output

@app.route('/contact')
def contact():
    output = render_template('contact.html')
    return output

@app.route('/base')
def base():
    with open("data.json", "r", encoding='utf-8') as f:
        contents = json.loads(f.read())
    data_x = contents.keys()
    output = render_template('base.html', data_x)
    return output


app.run(debug = True)