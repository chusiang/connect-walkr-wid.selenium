# Quick verify friend's Walkr WID with Selenium (Python)

This is a selenium script for quick open [walkr official website](http://walkrgame.com/en/community) and connect new friend's WID.

1. Setup Env.

        $ sudo easy_install pip
        $ sudo pip install --upgrade pip
        $ virtualenv --no-site-packages .venv
        $ . .venv/bin/activate
        (.venv)$ pip install selenium

1. Setting WID.

        $ cp setting.ini.sample setting.ini
        
        $ vim setting.ini
        [profile]
        ...
        my_wid = xxxxxxxxxxx
        
        [friends_wid]
        friends_wid1 = xxxxxxxxxxx
        friends_wid2 = xxxxxxxxxxx
        friends_wid3 = xxxxxxxxxxx
        ...

1. Run.

        # Use virtualenv.
        $ . .venv/bin/activate
        
        # Run.
        (.venv)$ python play.py


1. Review result

        $ tail -f runtime.log
        [2016-04-18 11:37:26,693] INFO: Load setting.
        [2016-04-18 11:39:12,342] INFO: Go to website.
        [2016-04-18 11:39:12,565] INFO: Keyin my WID: xxxxxxxxxxx
        [2016-04-18 11:39:12,680] INFO: Keyin new friend's WID: xxxxxxxxxxx
        [2016-04-18 11:39:12,821] INFO: Click verify buttion
        [2016-04-18 11:41:01,003] INFO: Keyin my WID: xxxxxxxxxxx
        [2016-04-18 11:41:01,095] INFO: Keyin new friend's WID: xxxxxxxxxxx
        [2016-04-18 11:41:01,226] INFO: Click verify buttion
        [2016-04-18 11:41:11,284] INFO: Keyin my WID: xxxxxxxxxxx
        [2016-04-18 11:41:11,467] INFO: Keyin new friend's WID: xxxxxxxxxxx
        ...

By the way, if you need a friend, you can join me (**ViXQdeva_Dk**).
