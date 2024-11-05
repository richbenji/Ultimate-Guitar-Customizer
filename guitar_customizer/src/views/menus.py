class GuitarOptions:
    # Options générales communes
    GUITAR_COLORS = (
        "sunburst", "cherry sunburst", "tobacco sunburst", "black", "white",
        "natural", "honey burst", "amber", "vintage white", "fiesta red",
        "surf green", "lake placid blue", "candy apple red", "olympic white",
        "midnight blue", "shell pink", "butterscotch blonde", "gold top",
        "silver sparkle", "blue sparkle", "wine red", "arctic white",
        "translucent blue", "translucent red", "translucent green",
        "transparent black", "sapphire blue", "quilted maple", "flame maple",
        "matte black", "gloss black", "ivory", "desert burst", "pelham blue",
        "aged cherry burst", "ebony", "charcoal burst", "forest green",
        "burgundy mist", "purple sparkle", "black cherry burst", "seafoam green"
    )

    PICKUP_TYPES = (
        "None", "Single Coil", "Humbucker", "P90", "Filter'Tron",
        "Wide Range Humbuckers", "Lipstick"
    )

    BODY_WOOD = (
        "Alder", "Black limba", "Koa", "Swamp Ash", "Mahogany", "Maple",
        "Basswood", "Poplar", "Korina", "Mahogany/Basswood Sandwich",
        "Walnut", "Sapele"
    )

    TOP_WOOD = (
        "Black limba", "Mahogany", "Plain maple", "Flamed maple",
        "Flamed spalted maple", "Quilted maple", "Buckeye burl",
        "Flamed koa", "Burled maple", "Poplar burl", "Swamp ash",
        "Zebrawood", "Figured claro walnut"
    )

    NECK_WOOD = (
        "Alder", "Swamp Ash", "Mahogany", "Maple", "Basswood", "Poplar",
        "Korina", "Mahogany/Basswood Sandwich", "Walnut", "Sapele"
    )

    FINGERBOARD_MATERIAL = (
        "Maple", "Rosewood", "Ebony", "Redwood", "Purpleheart", "Zebrawood",
        "Birdseye maple", "Roasted maple", "Flamed maple", "Roasted Birdseye maple",
        "Roasted flamed maple", "Palemoon ebony"
    )

    RADIUS = (
        "7.25\" (184 mm)", "9.5\" (241 mm)", "10\" (254 mm)", "12\" (305 mm)",
        "14\" (356 mm)", "16\" (406 mm)", "20\" (508 mm)",
        "compound 9.5\"-12\" (241 - 305 mm)",
        "compound 12\"-14\" (305 - 356 mm)",
        "compound 12\"-16\" (305 - 406 mm)"
    )

    GUITAR_BRANDS = (
        "Fender", "Gibson/Epiphone", "Ibanez", "Dean", "Jackson",
        "Charvel", "Kramer", "ESP/LTD", "B.C. Rich", "Kiesel",
        "Peavey", "Washburn", "Schecter", "Larry Carlton", "PRS",
        "Rickenbacker", "Solar", "Gretsch"
    )

    PICKUP_BRANDS = (
        "Seymour Duncan", "DiMarzio", "EMG", "Fluence", "Gibson",
        "Bill Lawrence", "Dean", "Fender", "Filter'Tron", "Schecter",
        "Sustainiac"
    )

    BRIDGE_TYPES = (
        "Tune-O-Matic", "Tune-O-Matic with strings through body",
        "Vintage vibrato", "Floyd Rose vibrato", "Bigsby vibrato"
    )

    # Méthodes pour chaque section d'options
    @classmethod
    def get_general_options(cls):
        return [
            ("Modèle", ["By brand", "Import"]),
            ("Marque", cls.GUITAR_BRANDS),
            ("Dexterity", ["Right-handed", "Left-handed"]),
            ("Strings", ["6", "7", "8", "9"]),
            ("Scale length", ["25.5\" (648 mm)", "24.75\" (629 mm)"]),
            ("Build", ["Hollow body", "Semi hollow body", "Solid body"]),
        ]

    @classmethod
    def get_body_options(cls):
        return [
            ("Body wood", cls.BODY_WOOD),
            ("Top wood", cls.TOP_WOOD),
            ("Top shape", ["arch top", "flat top"]),
            ("Colors", cls.GUITAR_COLORS),
            ("Body finish", ["Gloss", "Satin"]),
        ]

    @classmethod
    def get_neck_options(cls):
        return [
            ("Wood", cls.NECK_WOOD),
            ("Neck material", ["Maple", "Mahogany", "Rosewood"]),
            ("Neck construction", ["Set neck", "Bolt on neck", "Neck through"]),
            ("Neck Shape", ["C", "D", "Slim taper D", "U", "Hard V", "Medium V", "Soft V", "Asymmetrical"]),
            ("Neck finish", ["Gloss", "Satin"]),
            ("Fingerboard material", cls.FINGERBOARD_MATERIAL),
            ("Number of frets", ["21", "22", "24"]),
            ("Fret size", ["Small", "Vintage medium", "medium", "jumbo", "Super jumbo", "Narrow"]),
            ("Fret material", ["Nickel silver", "Gold", "Stainless steel", "Bronze"]),
            ("Radius", cls.RADIUS),
            ("Inlay shape", ["Dots", "Blocks"]),
            ("Inlay material", ["Mother of pearl", "Abalone"]),
            ("Nut material", ["Plastic", "Graphite", "Bone", "Synthetic bone", "Brass", "Titanium", "Wood"]),
            ("Headstock shape", ["Match original body"]),
            ("Headstock finish", ["Match body"]),
            ("Truss rod cover", ["Black", "Cream", "White", "Red tortoiseshell", "White pearloid", "Ebony", "Purpleheart"])
        ]

    @classmethod
    def get_electronics_options(cls):
        return [
            ("Bridge Pickup", cls.PICKUP_TYPES),
            ("Middle Pickup", cls.PICKUP_TYPES),
            ("Neck Pickup", cls.PICKUP_TYPES),
            ("Bridge Pickup brand", cls.PICKUP_BRANDS),
            ("Middle Pickup brand", cls.PICKUP_BRANDS),
            ("Neck Pickup brand", cls.PICKUP_BRANDS),
            ("Bobbin colors", []),
            ("Pickup pole pieces", ["Black", "Chrome", "Gold"]),
            ("Covers", ["None", "Black", "Chrome", "Gold"]),
            ("Direct mount", ["Yes", "No"]),
            ("Controls", ["Volume + Tone", "2 Volumes + Tone", "2 Volumes + 2 Tones", "Volume", "2 Volumes"]),
            ("Out of phase pickups", [])
        ]

    @classmethod
    def get_hardware_options(cls):
        return [
            ("Bridge", cls.BRIDGE_TYPES),
            ("Hardware color", ["Black", "Chrome", "Gold"]),
            ("Knobs", []),
            ("Strings", []),
            ("Electronics cavity cover", [])
        ]

    @classmethod
    def get_export_load_options(cls):
        return [
            ("Save", ["test"])
        ]

    @classmethod
    def get_all_section_options(cls):
        return {
            "General": cls.get_general_options(),
            "Body": cls.get_body_options(),
            "Neck": cls.get_neck_options(),
            "Electronics": cls.get_electronics_options(),
            "Hardware": cls.get_hardware_options(),
            "Export/Load": cls.get_export_load_options()
        }
