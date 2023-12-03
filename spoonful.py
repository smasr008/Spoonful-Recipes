import streamlit as st
import requests

def search_recipes(query):

    url = "https://yummly2.p.rapidapi.com/feeds/auto-complete"

    querystring = {"q":query}

    headers = {
        "X-RapidAPI-Key": "c2d937b9f2mshafbbd836058d5ecp18be9fjsn0c1f3c8d86a4",
        "X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
    return response.json()

def display_recipes(recipes):
    col1, col2, col3 = st.columns(3)


    option = st.radio('Select menu item:', recipes, on_change= itemSelected)
    print(option)
    

def display_graphs():
    # Code to display line graph and bar graph for most popular dishes
    pass

def itemSelected(selection):
    response = search_recipes(selection)
    print(response)


def main():
    st.title("Spoonful Recipes")
    options = ['Breakfast Recipes', 'Lunch Recipes', 'Dinner Recipes', 'Dessert Recipes']
    selected_option = st.selectbox('Choose a recipe type', options)

    search_input = st.text_input('Search for a recipe')
    search_button = st.button('Search')

    if search_button:
        if search_input:
            recipes = search_recipes(search_input)
            if recipes:
                st.success("Results found!")
                display_recipes(recipes["ingredients"])  # Displaying 6 recipes
                display_graphs()
            else:
                st.error("No results found.")
        else:
            st.warning("Please enter a search query.")

if __name__ == "__main__":
    main()
