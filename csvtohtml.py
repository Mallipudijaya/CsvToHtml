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
        <link href="https://cdn.datatables.net/1.12.1/css/jquery.dataTables.css" rel="stylesheet">
        <link href="https://cdn.datatables.net/fixedheader/3.2.4/css/fixedHeader.dataTables.css" rel="stylesheet">
        <link href="https://cdn.datatables.net/fixedColumns/4.2.1/css/fixedColumns.dataTables.css" rel="stylesheet">
    </header>
       
    <body>
     
    {table_html}
   
    <script src="https://code.jquery.com/jquery-3.6.1.js" ></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.js"></script>
    <script type="text/javascript" src="ColReorderWithResize.js"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/fixedcolumns/4.2.1/js/dataTables.fixedColumns.js"></script>
     <script type="text/javascript" src="https://cdn.datatables.net/fixedHeader/3.2.4/js/dataTables.fixedHeader.js"></script>
   

    <script>
        
        $(document).ready( function () {{
            $('#table').DataTable({{
               
                'dom': 'Rlfrtip',
            
               
            }});
            
           
        }});
    
    </script>
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
    