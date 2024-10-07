guitar_colors = (
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

pickup_types = (
    "None",
    "Single Coil",
    "Humbucker",
    "P90",
    "Filter'Tron",
    "Wide Range Humbuckers",
    "Lipstick")

body_wood = (
    "Alder",
    "Black limba",
    "Koa",
    "Swamp Ash",
    "Mahogany",
    "Maple",
    "Basswood",
    "Poplar",
    "Korina",
    "Mahogany/Basswood Sandwich",
    "Walnut",
    "Sapele"
)

top_wood = (
    "Black limba",
    "Mahogany",
    "Plain maple",
    "Flamed maple",
    "Flamed spatle maple",
    "Quilted maple",
    "Buckeye burl",
    "Flamed koa",
    "Burled maple",
    "Poplar burl",
    "Swamp ash",
    "Zebrawood",
    "Figured claro walnut"
)
neck_wood = (
    "Alder",
    "Swamp Ash",
    "Mahogany",
    "Maple",
    "Basswood",
    "Poplar",
    "Korina",
    "Mahogany/Basswood Sandwich",
    "Walnut",
    "Sapele"
)

fingerboard_material = (
    "Maple",
    "Rosewood",
    "Ebony",
    "Redwood",
    "Purpleheart",
    "Zebrawood",
    "Birdseye maple",
    "Roasted maple",
    "Flamed maple",
    "Roasted Birdseye maple",
    "Roasted flamed maple",
    "Palemoon ebony"
)

radius = (
    "7.25\" (184 mm)",
    "9.5\" (241 mm)",
    "10\" (254 mm)",
    "12\" (305 mm)",
    "14\" (356 mm)",
    "16\" (406 mm)",
    "20\" (508 mm)",
    "compound 9.5\"-12\" (241 - 305 mm)"
    "compound 12\"-14\" (305 - 356 mm)",
    "compound 12\"-16\" (305 - 406 mm)"
)
pickup_brand = (
    "Seymour Duncan",
    "DiMarzio",
    "EMG",
    "Fluence",
    "Gibson",
    "Bill Lawrence",
    "Dean",
    "Fender",
    "Filter'Tron",
    "Schecter",
    "Sustainiac"
 )

bridge = (
    "Tune-O-Matic",
    "Tune-O-Matic with strings through body",
    "Vintage vibrato",
    "Floyd Rose vibrato",
    "Bigsby vibrato"
)

section_options = {
    "General": [
        ("Dexterity", ["Right-handed", "Left-handed"]),
        ("Strings", ["6", "7", "8", "9"]),
        ("Scale length", ["25.5\" (648 mm)", "24.75\" (629 mm)"]),
        ("Build", ["Hollow body", "Semi hollow body",   "Solid body"])
    ],
    "Body": [
        ("Body wood", body_wood),
        ("Top wood", top_wood),
        ("Top shape", ["arch top", "flat top"]),
        ("Colors", guitar_colors),
        ("Body finish", ["Gloss", "Satin"])
    ],
    "Neck": [
        ("Wood", neck_wood),
        ("Neck material", ["Maple", "Mahogany", "Rosewood"]),
        ("Neck construction", ["Set neck", "Bolt on neck", "Neck through"]),
        ("Neck Shape", ["C", "D", "Slim taper D", "U", "Hard V", "Medium V", "Soft V", "Asymmetrical"]),
        ("Neck finish", ["Gloss", "Satin"]),
        ("Fingerboard material", fingerboard_material),
        ("Number of frets", ["21", "22", "24"]),
        ("Fret size", ["Small", "Vintage medium", "medium", "jumbo", "Super jumbo", "Narrow"]),
        ("Fret material", ["Nickel silver", "Gold", "Stainless steel", "Bronze"]),
        ("Radius", radius),
        ("Inlay shape", ["Dots", "Blocks"]),
        ("Inlay material", ["Mother of pearl", "Abalone"]),
        ("Nut material", ["Plastic", "Graphite", "Bone", "Synthetic bone", "Brass", "Titanium", "Wood"]),
        ("Headstock shape", ["Match original body"]),
        ("Headstock finish", ["Match body"]),
        ("Truss rod cover", ["Black", "Cream", "White", "Red tortoiseshell", "White pearloid", "Ebony", "Purpleheart"])
    ],
    "Electronics": [
        ("Bridge Pickup", pickup_types),
        ("Middle Pickup", pickup_types),
        ("Neck Pickup", pickup_types),
        ("Bridge Pickup brand", pickup_brand),
        ("Middle Pickup brand", pickup_brand),
        ("Neck Pickup brand", pickup_brand),
        ("Bobbin colors", []),
        ("Pickup pole pieces", ["Black", "Chrome", "Gold"]),
        ("Covers", ["None", "Black", "Chrome", "Gold"]),
        ("Controls", ["Volume + Tone", "2 Volumes + Tone", "2 Volumes + 2 Tones", "Volume", "2 Volumes"]),
        ("Out of phase pickups", [])
    ],
    "Hardware": [
        ("Bridge", bridge),
        ("Hardware color", ["Black", "Chrome", "Gold"]),
        ("Knobs", []),
        ("Strings", []),
        ("Electronics cavity cover", [])
    ]
}
