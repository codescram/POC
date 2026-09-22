from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Full 9-month roadmap with day number, short task, tech label
months = [
    # Month 1
    {'name':'Month 1 - JS Core + DOM', 'days':[ (i,f'Day {i} task summary','JS') for i in range(1,31) ]},
    # Month 2
    {'name':'Month 2 - TypeScript + Angular', 'days':[ (i+30,f'Day {i+30} task summary','TS/Angular') for i in range(1,31) ]},
    # Month 3
    {'name':'Month 3 - Angular Advanced + RxJS', 'days':[ (i+60,f'Day {i+60} task summary','Angular') for i in range(1,31) ]},
    # Month 4
    {'name':'Month 4 - React Fundamentals', 'days':[ (i+90,f'Day {i+90} task summary','React') for i in range(1,31) ]},
    # Month 5
    {'name':'Month 5 - React + TS + State', 'days':[ (i+120,f'Day {i+120} task summary','React+TS') for i in range(1,31) ]},
    # Month 6
    {'name':'Month 6 - Node.js Backend', 'days':[ (i+150,f'Day {i+150} task summary','Node') for i in range(1,30+1) ]},
    # Month 7
    {'name':'Month 7 - Fullstack Integration + SQL', 'days':[ (i+180,f'Day {i+180} task summary','Angular/React+Node+SQL') for i in range(1,31) ]},
    # Month 8
    {'name':'Month 8 - TS Backend + Advanced SQL + Python', 'days':[ (i+210,f'Day {i+210} task summary','TS+Node+SQL+Python') for i in range(1,31) ]},
    # Month 9
    {'name':'Month 9 - Python ML + Fullstack Capstone', 'days':[ (i+240,f'Day {i+240} task summary','Python+Fullstack') for i in range(1,31) ]}
]

# Color mapping
color_map = {
    'JS': colors.HexColor('#4A90E2'),
    'TS': colors.HexColor('#007ACC'),
    'TS/Angular': colors.HexColor('#3D405B'),
    'Angular': colors.HexColor('#3D405B'),
    'React': colors.HexColor('#F7DF1E'),
    'React+TS': colors.HexColor('#F7DF1E'),
    'Node': colors.HexColor('#339933'),
    'SQL': colors.HexColor('#996633'),
    'Angular/React+Node+SQL': colors.HexColor('#3D405B'),
    'TS+Node+SQL+Python': colors.HexColor('#007ACC'),
    'Python+Fullstack': colors.HexColor('#FF6F61'),
    'Project': colors.HexColor('#FFD700'),
    'Portfolio': colors.HexColor('#FF69B4')
}

# PDF setup
pdf_file = '9_month_roadmap.pdf'
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4
cell_width = width / 7
cell_height = (height-50) / 6  # 6 rows per month

for month in months:
    # Header
    c.setFont('Helvetica-Bold', 16)
    c.drawCentredString(width/2, height-30, month['name'])

    # Draw day blocks
    for idx, (day_num, task, tech) in enumerate(month['days']):
        row = idx // 7
        col = idx % 7
        x = col * cell_width
        y = height - 50 - (row+1)*cell_height

        c.setFillColor(color_map.get(tech, colors.lightgrey))
        c.rect(x, y, cell_width, cell_height, fill=1)

        # Day number
        c.setFillColor(colors.black)
        c.setFont('Helvetica-Bold', 10)
        c.drawString(x+2, y+cell_height-12, str(day_num))

        # Short task summary
        c.setFont('Helvetica', 8)
        c.drawCentredString(x + cell_width/2, y + cell_height/2, task)

    # Footer legend
    c.setFont('Helvetica', 8)
    legend_y = 10
    c.drawString(20, legend_y, 'Legend: JS=🟦 TS=🟦 Angular=🟩 React=🟨 Node=🟪 SQL=🟫 Python=🟥 Project=⚡ Portfolio=📝')

    c.showPage()

c.save()
print(f'PDF generated: {pdf_file}')
