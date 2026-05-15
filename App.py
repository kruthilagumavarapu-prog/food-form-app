import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Food Form")


# =========================
# SESSION INIT
# =========================
if "page" not in st.session_state:
    st.session_state.page = 1

sections = [
    "breakfast","veg","nonveg",
    "veg_gravy","nonveg_gravy",
    "veg_fry","veg_biryani","nonveg_biryani",
    "veg_flavored","nonveg_flavored",
    "accomp","desserts","traditional","regular"
]

for s in sections:
    if s not in st.session_state:
        st.session_state[s] = []

# =========================
# HANDLE FUNCTION
# =========================
def handle(option, key, store, label):

    limits = {
        "Breakfast": 2,

        "VEG": 1,
        "NON-VEG": 1,

        "Veg Gravy": 1,
        "Non-Veg Gravy": 1,

        "Veg Fry": 1,

        "Veg Biryani": 1,
        "Non-Veg Biryani": 1,

        "Veg Flavored": 1,
        "Non-Veg Flavored": 1,

        "Accompaniments": 1,
        "Desserts": 1,
        "Traditional": 1,
        "Regular": 1
    }

    max_limit = limits[label]

    if st.session_state[key]:
        if option not in store:
            if len(store) < max_limit:
                store.append(option)
            else:
                st.warning(f"⚠️ Only {max_limit} allowed in {label}")
                st.session_state[key] = False
    else:
        if option in store:
            store.remove(option)
# =========================
# PAGE 1
# =========================
if st.session_state.page == 1:
    st.title("👤 Employee Details")

    name = st.text_input("Full Name")
    dept = st.text_input("Department")
    email= st.text_input("Email")


    if st.button("Next ➡️"):
        if name and dept and email:
            st.session_state.name = name
            st.session_state.dept = dept
            st.session_state.email = email
            st.session_state.page = 2
        else:
            st.error("Fill all fields")

# =========================
# PAGE 2 - BREAKFAST
# =========================
if st.session_state.page == 2:
    st.title("🍽️ Breakfast")

    breakfast = [
    "Idli",
    "Mysore Bonda",
    "Vegetable Upma",
    "Punugulu",
    "Wada",
    "Pongal",
    "Poha",
    "Saboodana Kichidi",
    "Chole Poori",
    "Bread Pakoda",
    "Toast + Jam/Peanut Butter",
    "Veg Sandwich",
    "Oatmeal with Fruits or Nuts",
    "Mix Fruit Bowl",
    "Boiled Eggs"
]

    for i,opt in enumerate(breakfast):
        k=f"bf_{i}"
        st.checkbox(opt,key=k,on_change=handle,
                    args=(opt,k,st.session_state.breakfast,"Breakfast"))

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div style="display:flex; justify-content:center;">
            """,
            unsafe_allow_html=True
        )
        if st.button("⬅️ Back", key="back_3"):
            st.session_state.page = 2
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div style="display:flex; justify-content:center;">
            """,
            unsafe_allow_html=True
        )
        if st.button("Next ➡️", key="next_3"):
            st.session_state.page = 4
        st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PAGE 3 - LUNCH
# =========================
if st.session_state.page == 3:
    
    st.title("🍛 Lunch")
    
    st.title("🥗 Starters")
    
    veg_starters = [
    "Veg Manchurian",
    "Veg Bullets",
    "Mirchi Bhajji",
    "Masala Vada",
    "Gobi 65",
    "Gobi Manchuria",
    "Bhindi Peanut Fry",
    "Ginger Veg",
    "Achari Aloo"
]
    st.subheader("VEG")

    for i,opt in enumerate(veg_starters):
        k=f"veg_{i}"
        st.checkbox(opt,key=k,on_change=handle,
                    args=(opt,k,st.session_state.veg,"VEG"))

    nonveg_starters = [
    "Chicken Spring Rolls",
    "Chicken Shangai Rolls",
    "Chicken Tex Mex Rolls",
    "Chicken Burmese Parcel",
    "Chicken Manchurian",
    "Pepper Chicken",
    "Chilli Chicken",
    "Ginger Chicken",
    "Garlic Chicken",
    "Chicken 65",
    "Chicken Salt & Pepper",
    "Chicken Momos",
    "Egg Pakoda"
]
    st.subheader("NON-VEG")
    
    for i,opt in enumerate(nonveg_starters):
        k=f"nv_{i}"
        st.checkbox(opt,key=k,on_change=handle,
                    args=(opt,k,st.session_state.nonveg,"NON-VEG"))

    veg_gravy = [
    "Paneer Butter Masala",
    "Paneer Tikka Masala",
    "Kadai Paneer",
    "Palak Paneer",
    "Paneer Kolhapuri",
    "Paneer Chatpata",
    "Paneer Jalfrezi",
    "Paneer Khandhari",
    "Achari Paneer",
    "Paneer Hara Masala",
    "Paneer Pasanda",
    "Shahi Paneer",
    "Methi Paneer",
    "Paneer Khurchan",
    "Paneer Do Pyaza",
    "Nawabi Paneer",
    "Paneer Noorjahani",
    "Paneer Malai Kofta",
    "Paneer Methi Malai",
    "Paneer Methi Chaman",
    "Veg Makhani",
    "Kadai Veg",
    "Veg Chatpata",
    "Veg Kolhapuri",
    "Veg Do Pyaza",
    "Veg Jalfrezi",
    "Navaratan Korma",
    "Palak Sabji",
    "Vegetable Kofta",
    "Vegetable Kofta In Palak Gravy",
    "Gobi Mutter",
    "Bhindi Do Pyaza",
    "Aloo Do Pyaza",
    "Vegetable Do Pyaza",
    "Bhindi Amritsari",
    "Bhindi Jaipuri",
    "Bhindi Masala",
    "Aloo Gobi Masala",
    "Subzi Hara Masala",
    "Stuffed Capsicum Masala",
    "Tomato Ka Masala",
    "Kadi Pakodi",
    "Achari Aloo Curry",
    "Dum Aloo Curry",
    "Jeera Aloo Curry",
    "Aloo Methi Curry",
    "Aloo Gobi Adraki Curry",
    "Bharwan Aloo Fry",
    "Aloo Pattaghobi Fry",
    "Aloo Methi Fry",
    "Khus Khus Aloo Fry",
    "Aloo Gobi Fry",
    "Tawa Sabzi",
    "Bhagara Bhaigan",
    "Baigan Ka Bartha",
    "Methi Malai Mutter",
    "Corn Palak",
    "Corn Methi Malai",
    "Nizami Handi",
    "Phool Makhani Curry",
    "Corn Kaju Capsicum Curry",
    "Mutter Phool Kaju Curry",
    "Tomato Kaju",
    "Tomato Green Peas",
    "Tomato Drumstick Kaju",
    "Tomato Drumstick",
    "Drumstick Phool Makhani",
    "Drumstick Paneer",
    "Drumstick Kidney Beans",
    "Drumstick & Capsicum",
    "Drumstick Milk",
    "Beans Tomato",
    "Tomato Mushroom",
    "Beerakaya Kaju",
    "Beerakaya Sangapappu",
    "Beerakaya Ulavacharu",
    "Beerakaya Tomato",
    "Beerakaya Double Beans",
    "Beerakaya Mushroom",
    "Beerakaya Kidney Beans",
    "Beerakaya Drumstick",
    "Beerakaya Corn",
    "Sorakaya Coconut Chana Dal",
    "Chikkudukaya Tomato",
    "Drumstick Kaju",
    "Drumsticks",
    "Masala Vada",
    "Gobi Palak",
    "Capsicum Mushroom",
    "Capsicum Baby Corn",
    "Kaju Aloo Green Peas Corn",
    "Gobi Tomato",
    "Gobi Kidney Beans",
    "Gobi Double Beans",
    "Pesara Punugula Curry",
    "Capsicum Tomato Kidney",
    "Beans Mirapakaya Curry",
    "Beans Masala",
    "Vankaya Masala",
    "Vankaya Bhatani Masala",
    "Mushroom Kaju Masala",
    "Bhindi Masala",
    "Dondakaya Masala",
    "Guthi Vankaya",
    "Butter Guthvankaya",
    "Gongura Vankaya",
    "Till Vankaya",
    "Nethi Vankaya",
    "Dum Ka Vankaya",
    "Chinta Chiguru Vankaya",
    "Dondakaya Paneer",
    "Kanda Bachali Kura",
    "Raw Banana Pachi Mirchi",
    "Mudda Kura",
    "Tomato Chikkudukaya Fry",
    "Nellor Mix Vegetable Khorma",
    "Dum Ka Bhendi",
    "Drumstick Mushroom",
    "Aloo Korma",
    "Aloo Carrot Korma",
    "Aloo Babycorn Korma",
    "Aloo Greenpeas Korma",
    "Paneer Greenpeas Korma",
    "Paneer Capsicum",
    "Greenpeas Korma",
    "Aloo Carrot Capsicum Korma",
    "Aloo Capsicum Korma",
    "Aloo Greenpeas",
    "Paneer Capsicum Korma",
    "Paneer Carrot Capsicum Korma",
    "Paneer Babycorn",
    "Vegetable Korma",
    "Gobi Korma"
]
    st.subheader("🍲 Veg Gravy")
    
    for i,opt in enumerate(veg_gravy):
        st.checkbox(opt,key=f"vg_{i}",on_change=handle,
                    args=(opt,f"vg_{i}",st.session_state.veg_gravy,"Veg Gravy"))

    st.subheader("🍗 Non‑Veg Gravy")
    
    nonveg_gravy = [
    "Makhani Butter",
    "Chatpat",
    "Kolapuri",
    "Kandhari",
    "Chicken Shahi Korma",
    "Dum Ka Chicken",
    "Punjabi Chicken",
    "Achari Chicken",
    "Chicken Do Pyaza",
    "Chicken Kali Mirchi",
    "Saagwala Chicken",
    "Adraki Murg",
    "Kadai Chicken",
    "Murgh Methi",
    "Murgh Shimla Mirchi",
    "Tandoori Chicken Tikka Masala",
    "Chicken Fry",
    "Pepper Chicken Fry",
    "Chicken Niligiri Korma",
    "Kodi Korma",
    "Telangana Kodi Korma",
    "Alugadda Kodi Korma",
    "Palakura Kodi Korma",
    "Kothimeera Kodi Korma",
    "Gongura Chicken",
    "Chicken Munakkaya Curry",
    "Chettinadu Chicken"
]

    for i,opt in enumerate(nonveg_gravy):
        st.checkbox(opt,key=f"nvg_{i}",on_change=handle,
                    args=(opt,f"nvg_{i}",st.session_state.nonveg_gravy,"Non-Veg Gravy"))

    # ✅ VEG FRY (FULL)
    st.subheader("🔥 Veg Fry")
    
    veg_fry = [
    "Carrot Beans Porial Fry",
    "Carrot Porial Fry",
    "Carrot Green Peas Porial Fry",
    "Carrot Pesarapappu Fry",
    "Mixed Vegetable Porial Fry",
    "Beans Porial Fry",
    "Cabbage Porial Fry",
    "Cabbage Beans Porial Fry",
    "Cabbage Green Peas Porial Fry",
    "Gobi Porial Fry",
    "Carrot Cabbage Porial Fry",
    "Aloo Porial Fry",
    "Aloo Carrot Porial Fry",
    "Raw Banana Porial Fry",
    "Bhindi Peanut Fry",
    "Bhindi Boondi Fry",
    "Bhindi Coconut Fry",
    "Bhindi Dum Fry",
    "Bhindi Pakodi Fry",
    "Barwa Bhindi Fry",
    "Stuffed Bhindi Fry",
    "Muvva Bendakaya Fry",
    "Brinjal Dhaniya Fry",
    "Brinjal Dondakaya Fry",
    "Brinjal Chanagapappu Fry",
    "Vankaya Coconut Fry",
    "Brinjal Kothimira Karam Fry",
    "Vankaya Vadiyalu Fry",
    "Vankaya Pakodi Fry",
    "Stuffed Vankaya Fry",
    "Purnam Vankaya Fry",
    "Muvva Vankaya Fry",
    "Kothimira Vankaya Fry",
    "Kanda Vepudu Fry",
    "Kanda Fine Piece Fry",
    "Chamagadda Round Fry",
    "Chamadumpala Fry",
    "Chamadumpala Kaju Fry",
    "Aloo Thurumudu Fry",
    "Aloo Ginger Garlic Fry",
    "Aloo Gobi Fry",
    "Aloo Capsicum Fry",
    "Aloo Dum Fry",
    "Aloo 65 Fry",
    "Aloo Pepper Fry",
    "Aloo Fine Piece Fry",
    "Aloo Gobi Capsicum Fry",
    "Aloo Methikura Fry",
    "Raw Banana Fry",
    "Raw Banana Round Fry",
    "Raw Banana Dum Fry",
    "Raw Banana Mudda Kura Fry",
    "Gobi Palak Fry",
    "Gobi Kaju Fry",
    "Gobi Green Peas Fry",
    "Gobi Keema Fry",
    "Gobi Fry",
    "Gobi Pakodi Fry",
    "Gobi 65 Fry",
    "Carrot Fry",
    "Carrot Mushroom Fry",
    "Carrot Coconut Fry",
    "Carrot Ullikaram Fry",
    "Cabbage Pakodi Fry",
    "Cabbage Pesarapappu Fry",
    "Palakura Pesarapappu Fry",
    "Thotakura Liver Fry",
    "Mixed Leaf Liver Fry",
    "Capsicum Pakoda Fry",
    "Capsicum Channakaram Fry",
    "Capsicum Iguru Fry",
    "Mealmaker Green Peas Kaju Poratu Fry",
    "Panasa Pottu Capsicum Fry"
]

    for i,opt in enumerate(veg_fry):
        st.checkbox(opt,key=f"vfry_{i}",on_change=handle,
                    args=(opt,f"vfry_{i}",st.session_state.veg_fry,"Veg Fry"))


    
    st.title("🍚 Biryani")
    st.subheader("VEG")
    
    veg_biryani = [
    "Vegetable Dum Biryani",
    "Veg Manchurian Biryani",
    "Dum Biryani",
    "English Vegetable Biryani",
    "Tomato Vegetable Biryani",
    "Babycorn Dum Biryani",
    "Paneer Dum Biryani",
    "Mushroom Dum Biryani"
]
    for i,opt in enumerate(veg_biryani):
        st.checkbox(opt,key=f"vbir_{i}",
                    on_change=handle,
                    args=(opt,f"vbir_{i}",st.session_state.veg_biryani,"Veg Biryani"))

    st.subheader("🍗NON-VEG")
    
    nonveg_biryani = [
    "Chicken Biryani",
    "Chicken Fry Biryani",
    "Egg Biryani"
]
    for i,opt in enumerate(nonveg_biryani):
        st.checkbox(opt,key=f"nvbir_{i}",
                    on_change=handle,
                    args=(opt,f"nvbir_{i}",st.session_state.nonveg_biryani,"Non-Veg Biryani"))

    st.title("🍛 Flavored Rice")
    st.subheader("VEG")
    
    veg_flavored = [
    "Ulavacharu Vegetable",
    "Vegetable Pulao",
    "Kabuli Pulao",
    "Navaratan Pulao",
    "Jeera Peas Pulao",
    "Peas Pulao",
    "Aloo Gobi Tehari",
    "Aloo Peas Tehari",
    "Jeera Rice",
    "Veg Fried Rice",
    "Steamed Rice",
    "Pudina Rice",
    "Kothimira Rice",
    "Tomato Rice",
    "Coconut Rice",
    "Lemon Rice",
    "Vegetable Bread Pulao",
    "Tomato Vegetable Pulao",
    "Double Beans Pulao",
    "Tamarind Pulao",
    "Mango Pulihora",
    "Usirikaya Pulihora"
]
    for i,opt in enumerate(veg_flavored):
        st.checkbox(opt,key=f"vfr_{i}",
                    on_change=handle,
                    args=(opt,f"vfr_{i}",st.session_state.veg_flavored,"Veg Flavored"))

    st.subheader("NON-VEG")
    
    nonveg_flavored = [
    "Chicken Pulao",
    "Spicy Chicken Pulao",
    "Royyala Pulao",
    "Mutton Kheema Pulao",
    "Chicken Fried Rice",
    "Mix Non Veg Fried Rice"
]
    for i,opt in enumerate(nonveg_flavored):
        st.checkbox(opt,key=f"nvfr_{i}",
                    on_change=handle,
                    args=(opt,f"nvfr_{i}",st.session_state.nonveg_flavored,"Non-Veg Flavored"))

    st.subheader("🥄 Accompaniments")
    
    accomp = [
    "Dosakaya Tomato Chutney (Yellow Cucumber)",
    "Dosakaya Mukkala Chutney (Yellow Cucumber)",
    "Dosakaya Vankaya Chutney (Yellow Cucumber)",
    "Tomato Brinjal Chutney",
    "Tomato Beerakaya Chutney (Ridge Gourd)",
    "Beerakaya Dondakaya Mukkala Chutney",
    "Beerakaya Mukkala Chutney (Ridge Gourd)",
    "Beerakaya Chutney (Ridge Gourd)",
    "Pudhina Chutney (Coriander)",
    "Kothimeera Chutney (Coriander)",
    "Kothimeera Tomato Chutney",
    "Mango Thurumu Chutney",
    "Pudhina Tomato Chutney",
    "Tomato Chutney",
    "Dondakaya Chutney (Ivy Gourd)",
    "Dondakaya Mukkala Chutney (Ivy Gourd)",
    "Carrot Chutney",
    "Cabbage Chutney",
    "Gobi Mukkala Chutney",
    "Sorakaya Perugu Chutney",
    "Mango Mukkala Chutney",
    "Mango Coconut Thurumu Chutney",
    "Coconut Red Chilly Chutney",
    "Pandu Mirchi Chutney",
    "Carrot Thurumu Chutney",
    "South Indian Papad",
    "Masala Papad",
    "Fryums",
    "Mango Pickle",
    "Magaya Pickle",
    "Gongura Pickle",
    "Lemon Pickle",
    "Tomato Pickle",
    "Dosakaya Pickle (Yellow Cucumber)",
    "Dondakaya Pickle (Ivy Gourd)",
    "Mixed Vegetable Pickle",
    "Ginger Pickle",
    "Garlic Pickle",
    "Garlic Kaju Pickle",
    "Gobi Pickle",
    "Brinjal Pickle",
    "Onion Raita",
    "Mixed Veg Raita",
    "Tomato Raita",
    "Cucumber Raita",
    "Bhoondi Raita",
    "Pineapple Raita"
]
    for i,opt in enumerate(accomp):
        st.checkbox(opt,key=f"ac_{i}",
                    on_change=handle,
                    args=(opt,f"ac_{i}",st.session_state.accomp,"Accompaniments"))

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div style="display:flex; justify-content:center;">
            """,
            unsafe_allow_html=True
        )
        if st.button("⬅️ Back", key="back_3"):
            st.session_state.page = 2
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div style="display:flex; justify-content:center;">
            """,
            unsafe_allow_html=True
        )
        if st.button("Next ➡️", key="next_3"):
            st.session_state.page = 4
        st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PAGE 4 - DESSERTS
# =========================
if st.session_state.page == 4:
    
    st.title("🍨 Desserts")
    
    desserts = [
    "Gulab Jamun",
    "Kala Jamun",
    "Fruit Custard",
    "Besan Ki Barfi",
    "Carrot Ka Halwa",
    "Balushahi",
    "Gajar Ka Halwa",
    "Moong Dal Halwa",
    "Double Ka Meetha",
    "Jangri",
    "Kaddu Ki Kheer",
    "Khubani Ka Meetha",
    "Pineapple Kesari",
    "Rava Kesari",
    "Semiya Payasam",
    "Sabudhana Payasam",
    "Dal Payasam",
    "Rice Payasam",
    "Sweet Pongal",
    "Boondhi Laddu",
    "Rava Laddu",
    "Sweet Boondhi",
    "Motichoor Laddu"
]

    for i,opt in enumerate(desserts):
        st.checkbox(opt,key=f"des_{i}",on_change=handle,
                    args=(opt,f"des_{i}",st.session_state.desserts,"Desserts"))

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div style="display:flex; justify-content:center;">
            """,
            unsafe_allow_html=True
        )
        if st.button("⬅️ Back", key="back_3"):
            st.session_state.page = 2
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div style="display:flex; justify-content:center;">
            """,
            unsafe_allow_html=True
        )
        if st.button("Next ➡️", key="next_3"):
            st.session_state.page = 4
        st.markdown("</div>", unsafe_allow_html=True)
        
# =========================
# ✅ PAGE 5 - SUMMARY
# =========================
if st.session_state.page == 5:

    

    st.title("✅ Review Your Selections")

    
    st.write("### 👤 Employee Details")
    st.write("Name:", st.session_state.name)
    st.write("Department:", st.session_state.dept)
    st.write("Email:", st.session_state.email)

    

    st.write("### 🍽️ Breakfast")
    for item in st.session_state.breakfast:
        st.write(f"• {item}")

    st.write("### 🥗 Starters Veg")
    for item in st.session_state.veg:
        st.write(f"• {item}")

    st.write("### 🍗 Starters Non‑Veg")
    for item in st.session_state.nonveg:
        st.write(f"• {item}")

    st.write("### 🍛 Veg Gravy")
    for item in st.session_state.veg_gravy:
        st.write(f"• {item}")

    st.write("### 🍗 Non‑Veg Gravy")
    for item in st.session_state.nonveg_gravy:
        st.write(f"• {item}")

    st.write("### 🔥 Veg Fry")
    for item in st.session_state.veg_fry:
        st.write(f"• {item}")

    st.write("### 🍚 Biryani (Veg)")
    for item in st.session_state.veg_biryani:
        st.write(f"• {item}")

    st.write("### 🍗 Biryani (Non‑Veg)")
    for item in st.session_state.nonveg_biryani:
        st.write(f"• {item}")

    st.write("### 🍛 Flavored Rice (Veg)")
    for item in st.session_state.veg_flavored:
        st.write(f"• {item}")

    st.write("### 🍗 Flavored Rice (Non‑Veg)")
    for item in st.session_state.nonveg_flavored:
        st.write(f"• {item}")

    st.write("### 🥄 Accompaniments")
    for item in st.session_state.accomp:
        st.write(f"• {item}")

    st.write("### 🍨 Desserts")
    for item in st.session_state.desserts:
        st.write(f"• {item}")


    # ✅ Buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Back",key="back_5"):
            st.session_state.page = 4

    with col2:
        if st.button("✅ Submit",key="conform_5" ):
            st.success("✅ Form Submitted Successfully!")
            st.session_state.page = 1
