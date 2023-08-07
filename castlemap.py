import folium


places = {
    "Krąg": [53.4883, 15.9742],
    "Kobiór": [50.0592, 18.9422],
    "Nidzica": [53.3662, 20.4275],
    "Otmuchów": [50.5413, 17.1553],
    "Kliczków": [51.1279, 15.6218],
    "Grodziec": [50.9329, 15.8945],
    "Ryn": [53.9316, 21.6949],
    "Sobków": [50.8020, 20.6105],
    "Łagów Lubuski": [52.3118, 15.1325],
    "Oleśnica": [51.2103, 17.3838],
    "Bytów": [54.1706, 17.4919],
    "Janów Podlaski": [51.9495, 23.2029],
    "Giżycko": [54.0376, 21.7665],
    "Karpniki": [50.8647, 15.9309],
    "Dubiecko": [49.9771, 22.3594],
    "Łańcut": [50.0209, 22.2308],
    "Malbork": [54.0395, 19.0285],
    "Niedzica": [49.4205, 20.6502],
    "Ogrodzieńiec": [50.4525, 19.5443],
    "Oświęcim": [50.0343, 19.2104],
    "Pieskowa Skała": [50.2498, 19.8062],
    "Sanok": [49.5556, 22.2130],
    "Sorków": [51.1367, 19.9440],
    "Wiślica": [50.7915, 20.4921],
    "Baranów Sandomierski": [50.5645, 21.5509],
    "Będzin": [50.3262, 19.2362],
    "Czorsztyn": [49.4339, 20.3236],
    "Dźwinogród": [49.9034, 21.8387],
    "Golub-Dobrzyń": [53.1045, 18.8829],
    "Bolków": [50.9292, 16.2906],
    "Kórnik": [52.2431, 17.0894],
    "Ojcow": [50.2164, 19.7868],
    "Otwock": [52.1093, 21.2610],
    "Wiśnicz": [49.9292, 20.4128]
}

# Miejsca z dostępnością noclegów
highlighted_places = {
    "Malbork", "Książ", "Kliczków", "Czocha", "Łańcut", "Niedzica",
    "Ogrodzieńiec", "Pieskowa Skała", "Ryn", "Sanok", "Wiślica",
    "Baranów Sandomierski", "Czorsztyn", "Bolków", "Kórnik", "Ojcow", "Wiśnicz"
}

# Tworzenie mapy
m = folium.Map(location=[52.0690, 19.4803], zoom_start=6)  # Domyślna lokalizacja centrum Polski

for place, coordinates in places.items():
    google_search_url = f"https://www.google.com/search?q={place}+zamek+nocleg"
    
    html_content = f'''
    <div style="width: 100px; border: 2px solid white; padding: 2px 5px; border-radius: 5px; background-color: rgba(0, 0, 0, 0.6); display: flex; align-items: center; justify-content: center;">
        <a href="{google_search_url}" target="_blank" style="color: white; text-decoration: none;">{place}</a>
    </div>
    '''

    icon = folium.DivIcon(
        icon_size=(150, 36),
        icon_anchor=(50, 18),  # Zaktualizowane w związku ze zmienioną szerokością
        html=html_content
    )


    
    folium.Marker(
        location=coordinates,
        icon=icon
    ).add_to(m)

m.save("map.html")