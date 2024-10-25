


car_model = "Volkswagen Polo"
age_range = "27-34"
experience_range = "10-15"
reputation_range = "1-2"
traffic_range = "4-7"
trip_duration_minutes = 15


tariffs = {
    ("Volkswagen Polo", "20-27", "2-9", "1-2", "1-3"): 8,
    ("Volkswagen Polo", "20-27", "2-9", "1-2", "4-7"): 8.5,
    ("Volkswagen Polo", "20-27", "2-9", "3-5", "1-3"): 8.3,
    ("Volkswagen Polo", "20-27", "2-9", "3-5", "4-7"): 8.2,
    ("Volkswagen Polo", "27-34", "2-9", "1-2", "1-3"): 7.4,
    ("Volkswagen Polo", "27-34", "2-9", "1-2", "4-7"): 7.5,
    ("Volkswagen Polo", "27-34", "2-9", "3-5", "1-3"): 7.2,
    ("Volkswagen Polo", "27-34", "2-9", "3-5", "4-7"): 7.3,
    ("Volkswagen Polo", "27-34", "10-15", "1-2", "1-3"): 6.7,
    ("Volkswagen Polo", "27-34", "10-15", "1-2", "4-7"): 6.6,
    ("BMW X1", "20-27", "2-9", "1-2", "1-3"): 12,
    ("BMW X1", "20-27", "2-9", "1-2", "4-7"): 12.5,
    ("BMW X1", "20-27", "2-9", "3-5", "1-3"): 11.6,
    ("BMW X1", "20-27", "2-9", "3-5", "4-7"): 11.3,
    ("BMW X1", "27-34", "2-9", "1-2", "1-3"): 11.4,
    ("BMW X1", "27-34", "2-9", "1-2", "4-7"): 11.7,
    ("BMW X1", "27-34", "2-9", "3-5", "1-3"): 11.7,
    ("BMW X1", "27-34", "2-9", "3-5", "4-7"): 11.9,
    ("BMW X1", "27-34", "10-15", "1-2", "1-3"): 10.8,
    ("BMW X1", "27-34", "10-15", "1-2", "4-7"): 10.9,
}


tariff = tariffs.get((car_model, age_range, experience_range, reputation_range, traffic_range))

if tariff:
    
    price = tariff * trip_duration_minutes
    print(f"Стоимость вашей поездки составит {price} рублей.")
else:
    print("Тариф не найден для введённых данных.")
