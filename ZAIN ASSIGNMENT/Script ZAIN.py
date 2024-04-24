import pyodbc

def main():
    jdbc_url = 'DRIVER={SQL Server};SERVER=DESKTOP-IRSO487;DATABASE=person;UID=personal;PWD=setting;'

    salary_id_counter = 120
    department = 'Software R'
    amount = 10000000.00
    person_id = '1J'

    salary_month = '1-'
    try:
        connection = pyodbc.connect(jdbc_url)
        cursor = connection.cursor()

        counter = 2
        while counter <= 12:
            
            
            if counter == 2:
                salary_month = '1-February'
            elif counter == 3:
                salary_month = '1-March'
            elif counter == 4:
                salary_month = '1-April'
            elif counter == 5:
                amount *= 2
                salary_month = '1-May'
            elif counter == 6:
                salary_month = '1-June'
            elif counter == 7:
                salary_month = '1-July'
            elif counter == 8:
                salary_month = '1-August'
            elif counter == 9:
                amount *= 2
                salary_month = '1-September'
            elif counter == 10:
                salary_month = '1-October'
            elif counter == 11:
                salary_month = '1-November'
            elif counter == 12:
                salary_month = '1-December'

            salary_id = 'ASD' + str(salary_id_counter)
            insert_query = f"INSERT INTO salary (SalaryID, Amount, Department, SalaryMonth, PersonID) " \
                           f"VALUES ('{salary_id}', {amount}, '{department}', '{salary_month}', '{person_id}')"
            
            cursor.execute(insert_query)
            connection.commit()
            counter += 1
            salary_id_counter += 1

        connection.close()
        print("Data Updated Successfully.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
