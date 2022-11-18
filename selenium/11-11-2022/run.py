from booking.booking import Booking


# with Booking() as bot:
#     bot.land_first_page()
#     # bot.change_currency(currency='USD')
#     # bot.select_place_to_go('New York')
#     # bot.select_dates(check_in_date='2022-11-10',
#     #                  check_out_date='2022-11-25')
#     # bot.select_adults(4)
#     # bot.click_search()
#     # bot.apply_filtrations()


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='SAR')
