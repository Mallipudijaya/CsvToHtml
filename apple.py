import pandas as pd
import webbrowser

def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table")
    
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    <html>
    <header>
            <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
            <link href="https://nightly.datatables.net/css/jquery.dataTables.css" rel="stylesheet" type="text/css" />
            <link href="resizer.css" rel="stylesheet" type="text/css" />
            <script src="https://nightly.datatables.net/js/jquery.dataTables.js"></script>
            <script type = "text/javascript" src="exclude.js"></script> 
            <script type = "text/javascript" src="resize.js"></script>  

           
    </header>
    <body>
     <tr><td>Exclude: <input type="text" id="exc" name="exc" ></td></tr>
     <div class="horizontal-scroll-except-first-column">
    {table_html}
   </div>
   
    </body>
    </html>
    """
    # return the html
    return html


if __name__ == "__main__":
    # read the dataframe dataset
    df = pd.read_csv("airtravel.csv")
    # generate the HTML from the dataframe
    html = generate_html(df)
    # write the HTML content to an HTML file
    open("index.html", "w").write(html)
    # open the new HTML file with the default browser
    webbrowser.open("index.html")
    