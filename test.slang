yo gang homies be ["Tay", "Jay", "Ray"]
yo int hype = 0

spit "Roll call time!"

for name in homies {
    spit "Who's here?", name

    if (name == "Jay") {
        spit name , "brings the vibes."
        hype = hype + 1
    }
    if (name aint "Tay"){
    hype = hype -1
    }
    else {
        spit name , "is chillin'."
    }
}

spit "Hype level:", hype

when (hype > 0) {
    spit "Party's lit 🔥"
}
else {
    spit "Kinda lowkey tonight."
}
