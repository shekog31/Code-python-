def tw(BA,tip):
    ttl=BA*(1+0.01*tip)
    ttl=round(ttl,2)
    print(f"Pay {ttl}")
    
tw(108,15)