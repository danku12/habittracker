def kuva_statistika(harjumused):
    text="Statistika:\n\n"

    # фильтруем только числа (int/float)
    clean_data={}

    for nimi, kogus in harjumused.items():
        if isinstance(kogus, (int, float)):
            clean_data[nimi]=kogus
        else:
            clean_data[nimi]=0 

    sorted_harjumused=sorted(
        clean_data.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for nimi, kogus in sorted_harjumused:
        text+=f" - {nimi}: {kogus}\n"

    return text
