import flet as ft

def main(page: ft.Page):

    result = ft.Text(value="0", size=30)
    num1_ipt = ft.TextField(label="Enter a number", width=200)
    num2_ipt = ft.TextField(label="Enter another number", width=200)

    def add(_):
        try:
            num1 = float(num1_ipt.value)
            num2 = float(num2_ipt.value)
            result.value = str(num1 + num2)
            page.update()
        except ValueError:
            result.value = "Please enter valid numbers"
            page.update()

    def sub(_):
        try:
            num1 = float(num1_ipt.value)
            num2 = float(num2_ipt.value)
            result.value = str(num1 - num2)
            page.update()
        except ValueError:
            result.value = "Please enter valid numbers"
            page.update()

    def mult(_):
        try:
            num1 = float(num1_ipt.value)
            num2 = float(num2_ipt.value)
            result.value = str(num1 * num2)
            page.update()
        except ValueError:
            result.value = "Please enter valid numbers"
            page.update()

    def div(_):
        try:
            num1 = float(num1_ipt.value)
            num2 = float(num2_ipt.value)
            if num2 != 0:
                result.value = str(num1 / num2)
            else:
                result.value = "Sorry, can't divide by 0"
            page.update()
        except ValueError:
            result.value = "Please enter valid numbers"
            page.update()

    calc_btns = ft.Row(
        controls=[
            ft.ElevatedButton(text="+", on_click=add),
            ft.ElevatedButton(text="-", on_click=sub),
            ft.ElevatedButton(text="×", on_click=mult),
            ft.ElevatedButton(text="÷", on_click=div),
        ]
    )

    calc_tab = ft.Tab(
        text="Basic Calculator",
        content=ft.Column(
            controls=[
                num1_ipt,
                num2_ipt,
                calc_btns,
                result
            ],
        )
    )

    height_ipt = ft.TextField(label="What's your height (cm)?", width=200)
    weight_ipt = ft.TextField(label="What's your weight (kg)?", width=200)
    bmi_rslt = ft.Text(value="BMI: 0", size=30)

    def bmi_calc(_):
        try:
            height = float(height_ipt.value) / 100  
            weight = float(weight_ipt.value)
            bmi = weight / (height * height)
            bmi_rslt.value = "BMI: " + str(round(bmi, 1))

            if bmi < 18.5:
                bmi_rslt.value += "\nUnderweight"
            elif bmi < 25:
                bmi_rslt.value += "\nNormal weight"
            elif bmi < 30:
                bmi_rslt.value += "\nOverweight"
            else:
                bmi_rslt.value += "\nObese"

            page.update()
        except ValueError:
            bmi_rslt.value = "Please enter valid numbers"
            page.update()

    bmi_tab = ft.Tab(
        text="BMI Calculator",
        content=ft.Column(
            controls=[
                height_ipt,
                weight_ipt,
                ft.ElevatedButton(text="Calculate BMI", on_click=bmi_calc),
                bmi_rslt
            ],
        )
    )


    amount_ipt = ft.TextField(label="Enter amount", width=200)
    rslt_text = ft.Text(value="Result: 0", size=30)

    units = ft.Dropdown(
        width=200,
        label="Select the unit type",
        options=[
            ft.dropdown.Option("Length"),
            ft.dropdown.Option("Weight"),
        ],
    )

    from_unit = ft.Dropdown(
        width=200,
        label="From",
        options=[
            ft.dropdown.Option("cm"),
            ft.dropdown.Option("inches"),
            ft.dropdown.Option("kg"),
            ft.dropdown.Option("pounds"),
        ],
    )

    to_unit = ft.Dropdown(
        width=200,
        label="To",
        options=[
            ft.dropdown.Option("cm"),
            ft.dropdown.Option("inches"),
            ft.dropdown.Option("kg"),
            ft.dropdown.Option("pounds"),
        ],
    )

    def conv_units(_):
        try:
            amount = float(amount_ipt.value)

            if from_unit.value == "cm" and to_unit.value == "inches":
                result = amount * 0.394
            elif from_unit.value == "inches" and to_unit.value == "cm":
                result = amount * 2.54
            elif from_unit.value == "kg" and to_unit.value == "pounds":
                result = amount * 2.205
            elif from_unit.value == "pounds" and to_unit.value == "kg":
                result = amount * 0.454
            else:
                result = amount  

            rslt_text.value = f"Result: {round(result, 2)} {to_unit.value}"
            page.update()
        except ValueError:
            rslt_text.value = "Please enter a valid number"
            page.update()

    conv_tab = ft.Tab(
        text="Unit Converter",
        content=ft.Column(
            controls=[
                units,
                from_unit,
                to_unit,
                amount_ipt,
                ft.ElevatedButton(text="Convert", on_click=conv_units),
                rslt_text
            ],
        )
    )

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[calc_tab, bmi_tab, conv_tab]
    )

    page.add(tabs)

ft.app(main) 