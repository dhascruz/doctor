from pathlib import Path

from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf import FlexibleColumnWidthTable
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from decimal import Decimal
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from borb.pdf.canvas.color.color import HexColor, X11Color
from borb.pdf.pdf import PDF
from borb.pdf.canvas.layout.table.fixed_column_width_table import FixedColumnWidthTable as Table
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.canvas.layout.layout_element import Alignment
from datetime import datetime
import random
from borb.pdf.canvas.layout.image.image import Image


from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
from borb.pdf.canvas.layout.table.table import TableCell
from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from decimal import Decimal

# create an empty Document
pdf = Document()

# add an empty Page
page = Page()
pdf.add_page(page)

# use a PageLayout (SingleColumnLayout in this case)
layout = SingleColumnLayout(page)

# add a Paragraph object

#def _build_invoice_information():    
    #table_001 = Table(number_of_rows=5, number_of_columns=3)
    
    # table_001.add(Paragraph("[Street Address]"))    
    # table_001.add(Paragraph("Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))    
    # now = datetime.now()    
    # table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year)))
    
    # table_001.add(Paragraph("[City, State, ZIP Code]"))    
    # table_001.add(Paragraph("Invoice #", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
    # table_001.add(Paragraph("%d" % random.randint(1000, 10000)))   
    
    # table_001.add(Paragraph("[Phone]"))    
    # table_001.add(Paragraph("Due Date", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT))
    # table_001.add(Paragraph("%d/%d/%d" % (now.day, now.month, now.year))) 
    
    # table_001.add(Paragraph("[Email Address]"))    
    # table_001.add(Paragraph(" "))
    # table_001.add(Paragraph(" "))

    # table_001.add(Paragraph("[Company Website]"))
    # table_001.add(Paragraph(" "))
    # table_001.add(Paragraph(" "))

    #table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))    		
    #table_001.no_borders()
    #return table_001



def _build_billing_and_shipping_information():  
    #table_001 = Table(number_of_rows=6, number_of_columns=2)
    table_001 = Table(number_of_rows=6, number_of_columns=2)  
    for h in ["From:", "To:"]:  
        table_001.add(  
            TableCell(  
                Paragraph(h, font_color=X11Color("Black"), font="Helvetica-Bold" ),  
                #background_color=HexColor("BBBBBB"), 
                
            ))  
        
  
    table_001.add(Paragraph("Pasumai Indhiya"))        # BILLING  
    table_001.add(Paragraph(trans.name))        # SHIPPING  
    
    table_001.add(Paragraph("M71, Cactus Corporate Coworking, #173,"))          # BILLING  
    table_001.add(Paragraph("[Company Name]"))          # SHIPPING  
    
    table_001.add(Paragraph(" 2nd Floor, Block B, Tecci Park"))        # BILLING  
    table_001.add(Paragraph("[Street Address]"))        # SHIPPING  
    
    table_001.add(Paragraph(", OMR, Sholinganallur, Chennai, Tamil Nadu - 600119.")) # BILLING  
    table_001.add(Paragraph("[City, State, ZIP Code]")) # SHIPPING  
    
    
    
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))  
    table_001.no_borders()  
    return table_001

def _build_itemized_description_table():  
    table_001 = FlexibleColumnWidthTable(number_of_rows=11, number_of_columns=4)
    table_001.add( TableCell(
                Paragraph(
                    "S.no",
                    font_color=X11Color("White"),
                     
                    horizontal_alignment=Alignment.LEFT,
                ),
                background_color=HexColor("016934"),
                
                preferred_width=Decimal(5),
            ))   
    

    table_001.add( TableCell(
                Paragraph(
                    "Description",
                    font_color=X11Color("White"),
                     
                    horizontal_alignment=Alignment.CENTERED,
                ),
                background_color=HexColor("016934"),
                
                preferred_width=Decimal(280),
            )) 

    
    table_001.add( TableCell(
                Paragraph(
                    "Subscription Duration",
                    font_color=X11Color("White"),
                     
                    horizontal_alignment=Alignment.LEFT,
                ),
                background_color=HexColor("016934"),
                
                preferred_width=Decimal(100),
            )) 
    
    table_001.add( TableCell(
                Paragraph(
                    "Amount",
                    font_color=X11Color("White"),
                     
                    horizontal_alignment=Alignment.LEFT,
                ),
                background_color=HexColor("016934"),
                
                preferred_width=Decimal(60),
            )) 
     
    # for h in ["S.no", "Description", "Subscription Duration", "Amount"]:  
    #     table_001.add(  
    #         TableCell(  
    #             Paragraph(h, font_color=X11Color("White")),  
    #             background_color=HexColor("016934"),  
    #         )  
    #     )  
  
    odd_color = HexColor("FFFFFF")  
    even_color = HexColor("FFFFFF") 


    # table_001.add(TableCell(Paragraph("", background_color=HexColor("FFFFFF"))))  
    # table_001.add(TableCell(Paragraph("", background_color=HexColor("FFFFFF"))))  
    # table_001.add(TableCell(Paragraph("", background_color=HexColor("FFFFFF"))))  
    # table_001.add(TableCell(Paragraph("", background_color=HexColor("FFFFFF"))))


    
    table_001.add(TableCell(Paragraph("")))
    table_001.add(TableCell(Paragraph("")))
    table_001.add(TableCell(Paragraph("")))
    table_001.add(TableCell(Paragraph("")))

    table_001.add( TableCell(
                Paragraph(
                    "1",
                    
                    horizontal_alignment=Alignment.LEFT,
                ),
                
                preferred_width=Decimal(5),
            )) 

    table_001.add(TableCell(Paragraph("Paumai Indhiya monthly magazine", background_color=HexColor("FFFFFF"))))  
    table_001.add(TableCell(Paragraph("1 Year", background_color=HexColor("FFFFFF"))))  
    table_001.add(TableCell(Paragraph("Rs. 360", background_color=HexColor("FFFFFF"))) )
    # for row_number, item in enumerate([("1", 2, 50)]):  
    #     c = even_color if row_number % 2 == 0 else odd_color  
    #     table_001.add(TableCell(Paragraph(item[0]), background_color=c))  
    #     table_001.add(TableCell(Paragraph(str(item[1])), background_color=c))  
    #     table_001.add(TableCell(Paragraph("Rs " + str(item[2])), background_color=c))  
    #     table_001.add(TableCell(Paragraph("Rs. " + str(item[1] * item[2])), background_color=c))  
      
    # Optionally add some empty rows to have a fixed number of rows for styling purposes
    for row_number in range(3, 10):  
        c = even_color if row_number % 2 == 0 else odd_color  
        for _ in range(0, 4):  
            table_001.add(TableCell(Paragraph(" "), background_color=c))  
    table_001.add(TableCell(Paragraph("", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT  ),))  
    table_001.add(TableCell(Paragraph("", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT  ),))  
    table_001.add(TableCell(Paragraph("Total", font="Helvetica-Bold", horizontal_alignment=Alignment.RIGHT  ),))  
    table_001.add(TableCell(Paragraph("Rs. 360.00", horizontal_alignment=Alignment.LEFT)))  
    table_001.set_padding_on_all_cells(Decimal(2), Decimal(2), Decimal(2), Decimal(2))  
    table_001.no_borders()  
    return table_001
    

layout.add(    
        Image(        
        "https://pi.crtitp.com/images/logo.png",        
        width=Decimal(120),        
        height=Decimal(40),
        horizontal_alignment=Alignment.RIGHT,    
        ))


#layout.add(_build_invoice_information())

# Empty paragraph for spacing
layout.add(Paragraph(" "))

# Billing and shipping information table
layout.add(_build_billing_and_shipping_information())

# Itemized description
layout.add(_build_itemized_description_table())

layout.add(    
        Image(        
        "https://pi.crtitp.com/images/round_seal_pi.png",        
        width=Decimal(80),        
        height=Decimal(80),
        horizontal_alignment=Alignment.RIGHT,    
        ))



    
# # store the PDF
# with open(Path("output.pdf"), "wb") as pdf_file_handle:
#     PDF.dumps(pdf_file_handle, pdf)