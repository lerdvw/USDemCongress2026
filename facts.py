# -*- coding: utf-8 -*-
"""
Every date, figure and source the page shows: the single source of truth.

The page's words live in web/page.html. Wherever they need a number, a date
or a citation, they name an entry here and build.py fills it in:

    PAGE_FIGURES    every number and date the page prints, already formatted
    SOURCES         every source the page cites, keyed by a short name

Figures that follow from others (seat targets, totals, differences, counts,
roundings) are worked out from their inputs, never typed in, and
DERIVED_FIGURE_NAMES lists them so check.py can work each one out again and
refuse a copy typed into the template. Where sources disagree, the reading
used is recorded beside its source, with the others.
"""

from collections import namedtuple
from datetime import date
from fractions import Fraction
from math import ceil

# The day these facts were last checked against their sources.
FACTS_CHECKED_ON = date(2026, 10, 1)


# ===========================================================================
# Sources
# ===========================================================================

# published is the source's own date, or None for a standing page such as a
# government tool, a fact sheet or the Constitution.
Source = namedtuple("Source", ["title", "publisher", "published", "url"])

SOURCES = {
    # -- The election and Congress -----------------------------------------
    "constitution_article_1_section_7": Source(
        "The Constitution of the United States: A Transcription (Article I, Section 7: the veto and its override)",
        "National Archives", None,
        "https://www.archives.gov/founding-docs/constitution-transcript"),
    "senate_iran_veto_override_2020": Source(
        "Roll Call Vote 84, 116th Congress: overriding the veto of S.J.Res. 68 (U.S. forces in hostilities "
        "against Iran)",
        "U.S. Senate", date(2020, 5, 7),
        "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1162/vote_116_2_00084.htm"),
    "senate_class_2": Source(
        "Class II Senators (the seats up in 2026)",
        "U.S. Senate", None,
        "https://www.senate.gov/senators/Class_II.htm"),
    "ballotpedia_senate_2026": Source(
        "United States Senate elections, 2026 (including the Florida and Ohio special elections)",
        "Ballotpedia", None,
        "https://ballotpedia.org/United_States_Senate_elections,_2026"),

    # -- Registering and voting --------------------------------------------
    "texas_registration_deadline": Source(
        "Texas Secretary of State Reminds Voters: October 5 Deadline to Register to Vote in November "
        "General Election",
        "Texas Secretary of State", date(2026, 9, 28),
        "https://www.sos.state.tx.us/about/newsreleases/2026/092826.shtml"),
    "georgia_registration_deadline": Source(
        "Georgia General Election 2026 (last day to register: October 5)",
        "Georgia.gov", None,
        "https://georgia.gov/georgia-general-election-2026"),
    "ncsl_same_day_registration": Source(
        "Same-Day Voter Registration",
        "National Conference of State Legislatures", date(2026, 3, 27),
        "https://www.ncsl.org/elections-and-campaigns/same-day-voter-registration"),
    "voting_plan_study": Source(
        "Do you have a voting plan? Implementation intentions, voter turnout, and organic plan making "
        "(Nickerson and Rogers, Psychological Science 21:194-199, 2010)",
        "PubMed", None,
        "https://pubmed.ncbi.nlm.nih.gov/20424044/"),

    # -- Truth Revealed ----------------------------------------------------
    "house_vote_epstein_act": Source(
        "Roll Call 289: H.R. 4405, Epstein Files Transparency Act",
        "Clerk of the U.S. House of Representatives", date(2025, 11, 18),
        "https://clerk.house.gov/Votes/2025289"),
    "epstein_act_text": Source(
        "H.R. 4405, Epstein Files Transparency Act (enrolled text), Section 2(a)",
        "U.S. Government Publishing Office", None,
        "https://www.govinfo.gov/content/pkg/BILLS-119hr4405enr/html/BILLS-119hr4405enr.htm"),
    "cbs_epstein_files_ruling": Source(
        "Judge orders DOJ to either unredact more Epstein files or explain why they must stay blacked out",
        "CBS News", date(2026, 6, 26),
        "https://www.cbsnews.com/news/judge-orders-doj-unredact-more-epstein-files-or-explain-why-blanche/"),
    "doj_inspector_general_epstein_audit": Source(
        "DOJ OIG Announces Initiation of Audit of DOJ's Compliance with the Epstein Files Transparency Act",
        "U.S. Department of Justice, Office of the Inspector General", date(2026, 4, 23),
        "https://oig.justice.gov/news/doj-oig-announces-initiation-audit"),
    "bls_cpi_august_2026": Source(
        "Consumer Price Index, August 2026",
        "U.S. Bureau of Labor Statistics", date(2026, 9, 11),
        "https://www.bls.gov/news.release/archives/cpi_09112026.htm"),
    "new_york_fed_tariff_burden": Source(
        "Who Is Paying for the 2025 U.S. Tariffs?",
        "Federal Reserve Bank of New York, Liberty Street Economics", date(2026, 2, 12),
        "https://libertystreeteconomics.newyorkfed.org/2026/02/who-is-paying-for-the-2025-u-s-tariffs/"),
    "politifact_iran_war_timeline": Source(
        "How long will the Iran war last? See Trump's timeline shift",
        "PolitiFact", date(2026, 3, 30),
        "https://politifact.com/article/2026/mar/30/trump-hegseth-iran-war-timeline/"),
    "msnbc_homan_investigation": Source(
        "Tom Homan was investigated for accepting $50,000 from undercover FBI agents. Trump's DOJ shut it down.",
        "MSNBC (Carol Leonnig and Ken Dilanian)", date(2025, 9, 20),
        "https://www.ms.now/msnbc/news/tom-homan-cash-contracts-trump-doj-investigation-rcna232568"),
    "nbc_adams_case_dismissed": Source(
        "NYC Mayor Eric Adams' corruption case dismissed; judge says charges can't be used as 'leverage'",
        "NBC News", date(2025, 4, 2),
        "https://www.nbcnews.com/news/us-news/eric-adams-corruption-case-permanently-dismissed-rcna199266"),
    "notus_public_integrity_section": Source(
        "The Justice Department Had 36 Lawyers Fighting Corruption Full-Time. Under Trump, It's Down to Two.",
        "NOTUS (Jose Pagliery), reprinted by The Washington Sun", date(2025, 9, 22),
        "https://washingtonsun.com/courts/doj-public-integrity"),
    "crs_congressional_subpoenas": Source(
        "Congressional Subpoenas: Enforcing Executive Branch Compliance (R45653)",
        "Congressional Research Service, via EveryCRSReport", date(2019, 3, 27),
        "https://www.everycrsreport.com/reports/R45653.html"),

    # -- Tariffs Repealed --------------------------------------------------
    "supreme_court_tariff_ruling": Source(
        "Learning Resources, Inc. v. Trump, No. 24-1287 (syllabus)",
        "Supreme Court of the United States", date(2026, 2, 20),
        "https://www.supremecourt.gov/opinions/25pdf/24-1287_4gcj.pdf"),
    "tax_foundation_tariff_tracker": Source(
        "Tracking the Impact of the Trump Tariffs & Trade War",
        "Tax Foundation", date(2026, 9, 10),
        "https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/"),
    "e2_clean_energy_cancellations": Source(
        "Clean Economy Works: June-May 2026 Analysis",
        "E2 (Environmental Entrepreneurs)", date(2026, 7, 20),
        "https://e2.org/reports/clean-economy-works-june-may-2026-2/"),
    "bls_wind_technician_pay": Source(
        "Wind Turbine Technicians, Occupational Outlook Handbook",
        "U.S. Bureau of Labor Statistics", None,
        "https://www.bls.gov/ooh/installation-maintenance-and-repair/wind-turbine-technicians.htm"),
    "cbo_2025_law_by_income": Source(
        "How the 2025 Reconciliation Act (Public Law 119-21) Will Affect the Distribution of Resources "
        "Available to Households",
        "Congressional Budget Office", date(2025, 8, 11),
        "https://www.cbo.gov/interactive/2025-reconciliation-act"),
    "kff_2026_marketplace_premiums": Source(
        "What We Know So Far About 2026 ACA Marketplace Enrollment, Premiums, and Deductibles",
        "KFF", date(2026, 5, 19),
        "https://www.kff.org/affordable-care-act/what-we-know-so-far-about-2026-aca-marketplace-enrollment-premiums-and-deductibles/"),

    # -- Truce Sealed ------------------------------------------------------
    "cbs_oman_mediator_deal_within_reach": Source(
        "U.S.-Iran deal is \"within our reach,\" Omani mediator says",
        "CBS News (Margaret Brennan and Joe Walsh)", date(2026, 2, 27),
        "https://www.cbsnews.com/news/us-iran-deal-within-our-reach-oman-mediator-says/"),
    "intercept_iran_war_casualties": Source(
        "U.S. Has Suffered More Casualties In Iran Since the Conclusion of Operation Epic Fury",
        "The Intercept", date(2026, 9, 28),
        "https://theintercept.com/2026/09/28/iran-war-us-casualties-operation-epic-fury/"),
    "cnn_iran_war_cost": Source(
        "Iran war has cost $45.1 billion, Pentagon tells Congress",
        "CNN", date(2026, 9, 18),
        "https://www.cnn.com/2026/09/18/politics/us-iran-war-cost"),
    "roll_call_iran_war_cost": Source(
        "Pentagon's latest Iran war cost estimate: $43.6 billion",
        "CQ Roll Call", date(2026, 9, 18),
        "https://rollcall.com/2026/09/18/pentagons-latest-iran-war-cost-estimate-43-6-billion/"),
    "aaa_gas_prices": Source(
        "National average gas prices",
        "AAA", date(2026, 10, 1),
        "https://gasprices.aaa.com/"),
    "senate_iran_war_powers_votes": Source(
        "Roll Call Votes, 119th Congress, 2nd Session: votes 184 (H.Con.Res. 86) and 244 (H.Con.Res. 89)",
        "U.S. Senate", None,
        "https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_119_2.htm"),
    "crs_conflict_with_iran": Source(
        "U.S. Conflict with Iran (R48887)",
        "Congressional Research Service", None,
        "https://www.congress.gov/crs-product/R48887"),
    "arms_control_jcpoa_limits": Source(
        "The Joint Comprehensive Plan of Action (JCPOA) at a Glance",
        "Arms Control Association", None,
        "https://www.armscontrol.org/factsheets/JCPOA-at-a-glance"),
    "arms_control_iran_timeline": Source(
        "Timeline of Nuclear Diplomacy With Iran",
        "Arms Control Association", None,
        "https://www.armscontrol.org/factsheets/Timeline-of-Nuclear-Diplomacy-With-Iran"),
}


# ===========================================================================
# The election
# ===========================================================================

# The Tuesday after the first Monday in November (2 U.S.C. 7); check.py
# works it out again from that rule.
ELECTION_DAY = date(2026, 11, 3)

# Texas and Georgia both close registration on this day (their own sites).
TEXAS_AND_GEORGIA_REGISTRATION_DEADLINE = date(2026, 10, 5)


# ===========================================================================
# Congress, and what "veto-proof" takes
# ===========================================================================

HOUSE_SEATS = 435
SENATE_SEATS = 100

# Article I, Section 7: a bill the president vetoes still becomes law if
# two-thirds of each chamber votes for it again. The share is of members
# voting, so these targets assume every seat is filled and every member votes.
VETO_OVERRIDE_SHARE = Fraction(2, 3)


def seats_for_share(seats_in_chamber, share):
    """The fewest seats that make up at least `share` of the chamber."""
    return ceil(seats_in_chamber * share)


HOUSE_SEATS_FOR_VETO_PROOF_MAJORITY = seats_for_share(HOUSE_SEATS, VETO_OVERRIDE_SHARE)
SENATE_SEATS_FOR_VETO_PROOF_MAJORITY = seats_for_share(SENATE_SEATS, VETO_OVERRIDE_SHARE)

# The precedent: in 2020 Congress passed S.J.Res. 68, ordering U.S. forces out
# of hostilities against Iran that it had not authorized. The President vetoed
# it, and the Senate's override vote on 7 May 2020 fell short of two-thirds.
IRAN_2020_OVERRIDE_VOTE_YEAS = 49
IRAN_2020_OVERRIDE_VOTE_NAYS = 44

# Every House seat is elected every two years. In the Senate, the 33 seats of
# Class 2 are up, plus two special elections for the rest of terms left in
# 2025: Ohio's (JD Vance became Vice President) and Florida's (Marco Rubio
# became Secretary of State). Each race is (state, kind of race, party that
# holds the seat now), the party read from senate.gov's class lists on 1 Oct.
SENATE_CLASS_UP_IN_2026_SEATS = 33
SENATE_RACES_2026 = [
    ("Alabama", "regular", "R"),
    ("Alaska", "regular", "R"),
    ("Arkansas", "regular", "R"),
    ("Colorado", "regular", "D"),
    ("Delaware", "regular", "D"),
    ("Florida", "special", "R"),
    ("Georgia", "regular", "D"),
    ("Idaho", "regular", "R"),
    ("Illinois", "regular", "D"),
    ("Iowa", "regular", "R"),
    ("Kansas", "regular", "R"),
    ("Kentucky", "regular", "R"),
    ("Louisiana", "regular", "R"),
    ("Maine", "regular", "R"),
    ("Massachusetts", "regular", "D"),
    ("Michigan", "regular", "D"),
    ("Minnesota", "regular", "D"),
    ("Mississippi", "regular", "R"),
    ("Montana", "regular", "R"),
    ("Nebraska", "regular", "R"),
    ("New Hampshire", "regular", "D"),
    ("New Jersey", "regular", "D"),
    ("New Mexico", "regular", "D"),
    ("North Carolina", "regular", "R"),
    ("Ohio", "special", "R"),
    ("Oklahoma", "regular", "R"),
    ("Oregon", "regular", "D"),
    ("Rhode Island", "regular", "D"),
    ("South Carolina", "regular", "R"),
    ("South Dakota", "regular", "R"),
    ("Tennessee", "regular", "R"),
    ("Texas", "regular", "R"),
    ("Virginia", "regular", "D"),
    ("West Virginia", "regular", "R"),
    ("Wyoming", "regular", "R"),
]
SENATE_RACE_COUNT = len(SENATE_RACES_2026)

# Not shown on the page: each chamber today, so check.py can print how far a
# veto-proof Democratic majority is. Read 1 Oct 2026 from senate.gov's three
# class lists (https://www.senate.gov/senators/Class_I.htm, _II, _III) and the
# House Press Gallery (https://pressgallery.house.gov/member-data/party-breakdown).
SENATE_DEMOCRATS_NOW = 45
SENATE_INDEPENDENTS_NOW = 2                  # Sanders and King, who caucus with the Democrats
SENATE_REPUBLICANS_NOW = 53
HOUSE_DEMOCRATS_NOW = 214
HOUSE_REPUBLICANS_NOW = 218
HOUSE_INDEPENDENTS_NOW = 1
HOUSE_VACANCIES_NOW = 2                      # TX-23 and FL-20


# ===========================================================================
# Truth Revealed: the questions that need answers under oath
# ===========================================================================

# The Epstein Files Transparency Act (H.R. 4405), as the House passed it.
EPSTEIN_ACT_HOUSE_YEAS = 427
EPSTEIN_ACT_HOUSE_NAYS = 1
EPSTEIN_ACT_DAYS_TO_PUBLISH = 30          # Section 2(a): "Not later than 30 days after ... enactment"

# Prices: BLS, the 12 months to August 2026, not seasonally adjusted.
PRICES_PERCENT_RISE_ALL_ITEMS = 3.4
PRICES_PERCENT_RISE_GASOLINE = 27.4
PRICES_PERCENT_RISE_ELECTRICITY = 3.8

# Who paid for the 2025 tariffs: "nearly 90 percent of the tariffs' economic
# burden fell on U.S. firms and consumers" (New York Fed, 12 Feb 2026).
US_SHARE_OF_2025_TARIFF_COST_PERCENT = 90       # "nearly"

# The war's promised length: "Well, we intended four to five weeks," said on
# this day to The New York Times (as quoted by PolitiFact).
FOUR_TO_FIVE_WEEKS_REMARK_DAY = date(2026, 3, 1)


def whole_months_between(earlier_day, later_day):
    """Complete calendar months from one day to a later one."""
    months = (later_day.year - earlier_day.year) * 12 + (later_day.month - earlier_day.month)
    if later_day.day < earlier_day.day:
        months -= 1
    return months


MONTHS_SINCE_FOUR_TO_FIVE_WEEKS_REMARK = whole_months_between(FOUR_TO_FIVE_WEEKS_REMARK_DAY, FACTS_CHECKED_ON)

# Bribery: the cash in the 2024 FBI sting MSNBC reported, and the Justice
# Department's Public Integrity Section in 2025. Two readings of its size:
#   NOTUS, 22 Sep 2025:              36 full-time lawyers in January, 2 by September (used)
#   Sen. Whitehouse, 13 Jul 2026:    "reportedly" forty, down to two
HOMAN_STING_CASH_DOLLARS = 50_000
PUBLIC_INTEGRITY_LAWYERS_START_2025 = 36
PUBLIC_INTEGRITY_LAWYERS_SEPTEMBER_2025 = 2


# ===========================================================================
# Tariffs Repealed: prices, jobs, and working families
# ===========================================================================

# Tariffs' cost per household in 2026. Two estimates, which measure different
# things; the page uses the Tax Foundation's:
#   Tax Foundation, 10 Sep 2026:  $820 per US household in 2026 (used)
#   Yale Budget Lab, 24 Aug 2026: "about $1,100 annually", over the medium
#                                 run (read by research only; its interactive
#                                 page could not be re-read for this check)
TARIFF_COST_PER_HOUSEHOLD_2026_DOLLARS = 820

# The highest tariffs still in force after the Supreme Court's ruling, under
# Section 232 (Tax Foundation's list, 10 Sep 2026).
TARIFF_RATE_STEEL_ALUMINUM_COPPER_PERCENT = 50
TARIFF_RATE_PATENTED_DRUGS_PERCENT = 100

# Clean-energy projects since January 2025 (E2, 20 Jul 2026): those
# cancelled, and those newly announced over the same time. The page says the
# cancellations outweigh the announcements in both investment and jobs;
# check.py holds it to that. (By count of projects they do not: 214 to 236.)
CLEAN_ENERGY_PROJECTS_CANCELLED = 214
CLEAN_ENERGY_INVESTMENT_CANCELLED_BILLIONS = 84.3
CLEAN_ENERGY_JOBS_CANCELLED = 160_561
CLEAN_ENERGY_PROJECTS_ANNOUNCED = 236
CLEAN_ENERGY_INVESTMENT_ANNOUNCED_BILLIONS = 59.8
CLEAN_ENERGY_JOBS_ANNOUNCED = 128_999

# Median annual pay, May 2025 (BLS).
WIND_TURBINE_TECHNICIAN_MEDIAN_PAY_DOLLARS = 64_120
ALL_WORKERS_MEDIAN_PAY_DOLLARS = 50_980

# The 2025 tax-and-spending law, average yearly change per household over
# 2026-2034, in 2025 dollars: the lowest and highest income tenths in CBO's
# interactive table, "Annual average change per household" (read 1 Oct 2026).
LOWEST_TENTH_YEARLY_CHANGE_DOLLARS = -1_214
HIGHEST_TENTH_YEARLY_CHANGE_DOLLARS = 13_622

# ACA marketplace premiums after tax credits, 2025 to 2026 (KFF, 19 May 2026).
MARKETPLACE_PREMIUM_PERCENT_RISE_2026 = 58
MARKETPLACE_MONTHLY_PREMIUM_2025_DOLLARS = 113
MARKETPLACE_MONTHLY_PREMIUM_2026_DOLLARS = 178


# ===========================================================================
# Truce Sealed: the Iran war, and the diplomacy that came before it
# ===========================================================================

# The day before the war: Oman's foreign minister, mediating, told CBS that
# Iran had agreed to "zero stockpiling" with "full verification", technical
# talks were set for Monday in Vienna, and the President said "no enrichment".
MEDIATOR_BREAKTHROUGH_DAY = date(2026, 2, 27)
IRAN_WAR_START = date(2026, 2, 28)                 # US-Israeli strikes begin (Operation Epic Fury)

# The Pentagon's own counts, as The Intercept reported them on 28 Sep. ABC
# News gave 18 dead on 1 Oct, and officials have alleged an undercount; the
# page uses the Pentagon's figures.
IRAN_WAR_US_DEATHS = 19
IRAN_WAR_US_KILLED_OR_WOUNDED = 880

# The cost the Pentagon reported to Congress on 18 Sep.
IRAN_WAR_COST_THROUGH_SEPTEMBER_3_BILLIONS = 43.6   # CQ Roll Call
IRAN_WAR_EXTRA_FUEL_BILLIONS = 1.5                  # CNN, from the same report

IRAN_WAR_COST_BILLIONS = round(IRAN_WAR_COST_THROUGH_SEPTEMBER_3_BILLIONS + IRAN_WAR_EXTRA_FUEL_BILLIONS, 1)

# Regular gasoline, national average (AAA, read 1 Oct 2026).
GAS_PRICE_TODAY_DOLLARS = 4.4137
GAS_PRICE_YEAR_AGO_DOLLARS = 3.1605

# Congress's votes on ordering US forces out of hostilities with Iran. The
# House has voted six times and passed three (CRS R48887); the Senate's two
# votes on such resolutions from the House are below (senate.gov).
HOUSE_IRAN_WAR_RESOLUTIONS_PASSED = 3
SENATE_IRAN_VOTE_JUNE_23_YEAS = 50                 # H.Con.Res. 86, agreed to
SENATE_IRAN_VOTE_JUNE_23_NAYS = 48
SENATE_IRAN_VOTE_SEPTEMBER_24_YEAS = 49            # H.Con.Res. 89, rejected
SENATE_IRAN_VOTE_SEPTEMBER_24_NAYS = 50

# The 2015 nuclear deal's limits, which the IAEA found Iran within until 2019.
JCPOA_ENRICHMENT_CAP_PERCENT = 3.67
JCPOA_STOCKPILE_CAP_KILOGRAMS = 300


# ===========================================================================
# What the template prints
# ===========================================================================

def long_date(day):
    """2026-11-03 as "November 3, 2026"."""
    return f"{day:%B} {day.day}, {day.year}"


def month_and_day(day):
    """2026-10-05 as "October 5"."""
    return f"{day:%B} {day.day}"


def whole_dollars(amount):
    """1214 as "$1,214"."""
    return f"${amount:,}"


def dollars_and_cents(amount):
    """4.4137 as "$4.41"."""
    return f"${amount:,.2f}"


def vote_tally(yeas, nays):
    """A vote as "50–48", kept on one line: word joiners (U+2060) stop a break at the dash."""
    return f"{yeas}\u2060–\u2060{nays}"


def count_in_words(count):
    """Small counts as a reader would write them: 3 as "three"."""
    return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve"][count]


PAGE_FIGURES = {
    # Dates
    "election_day_iso": ELECTION_DAY.isoformat(),
    "election_day_long": f"{ELECTION_DAY:%A}, {long_date(ELECTION_DAY)}",
    "election_day_medium": f"{ELECTION_DAY:%A}, {month_and_day(ELECTION_DAY)}",
    "election_day_short": month_and_day(ELECTION_DAY),
    "election_year": str(ELECTION_DAY.year),
    "facts_checked_on_long": long_date(FACTS_CHECKED_ON),
    "texas_and_georgia_registration_deadline": month_and_day(TEXAS_AND_GEORGIA_REGISTRATION_DEADLINE),

    # Congress
    "house_seats": str(HOUSE_SEATS),
    "senate_seats": str(SENATE_SEATS),
    "house_seats_for_veto_proof_majority": str(HOUSE_SEATS_FOR_VETO_PROOF_MAJORITY),
    "senate_seats_for_veto_proof_majority": str(SENATE_SEATS_FOR_VETO_PROOF_MAJORITY),
    "senate_race_count": str(SENATE_RACE_COUNT),
    "iran_2020_override_vote": vote_tally(IRAN_2020_OVERRIDE_VOTE_YEAS, IRAN_2020_OVERRIDE_VOTE_NAYS),

    # Voting
    "voting_plan_turnout_gain_points": "4.1",      # Nickerson and Rogers (2010), abstract

    # Truth Revealed
    "epstein_act_house_vote": vote_tally(EPSTEIN_ACT_HOUSE_YEAS, EPSTEIN_ACT_HOUSE_NAYS),
    "epstein_act_days_to_publish": str(EPSTEIN_ACT_DAYS_TO_PUBLISH),
    "prices_percent_rise_all_items": f"{PRICES_PERCENT_RISE_ALL_ITEMS}%",
    "prices_percent_rise_gasoline": f"{PRICES_PERCENT_RISE_GASOLINE}%",
    "prices_percent_rise_electricity": f"{PRICES_PERCENT_RISE_ELECTRICITY}%",
    "us_share_of_2025_tariff_cost": f"nearly {US_SHARE_OF_2025_TARIFF_COST_PERCENT} percent",
    "four_to_five_weeks_remark_day": month_and_day(FOUR_TO_FIVE_WEEKS_REMARK_DAY),
    "months_since_four_to_five_weeks_remark": count_in_words(MONTHS_SINCE_FOUR_TO_FIVE_WEEKS_REMARK).capitalize(),
    "homan_sting_cash": whole_dollars(HOMAN_STING_CASH_DOLLARS),
    "public_integrity_lawyers_start_2025": str(PUBLIC_INTEGRITY_LAWYERS_START_2025),
    "public_integrity_lawyers_september_2025": count_in_words(PUBLIC_INTEGRITY_LAWYERS_SEPTEMBER_2025),

    # Tariffs Repealed
    "tariff_cost_per_household_2026": whole_dollars(TARIFF_COST_PER_HOUSEHOLD_2026_DOLLARS),
    "tariff_rate_steel_aluminum_copper": f"{TARIFF_RATE_STEEL_ALUMINUM_COPPER_PERCENT} percent",
    "tariff_rate_patented_drugs": f"{TARIFF_RATE_PATENTED_DRUGS_PERCENT} percent",
    "clean_energy_projects_cancelled": str(CLEAN_ENERGY_PROJECTS_CANCELLED),
    "clean_energy_investment_cancelled": f"${CLEAN_ENERGY_INVESTMENT_CANCELLED_BILLIONS} billion",
    "clean_energy_jobs_cancelled": f"{CLEAN_ENERGY_JOBS_CANCELLED:,}",
    "wind_turbine_technician_median_pay": whole_dollars(WIND_TURBINE_TECHNICIAN_MEDIAN_PAY_DOLLARS),
    "all_workers_median_pay": whole_dollars(ALL_WORKERS_MEDIAN_PAY_DOLLARS),
    "lowest_tenth_yearly_loss": whole_dollars(-LOWEST_TENTH_YEARLY_CHANGE_DOLLARS),
    "highest_tenth_yearly_gain": whole_dollars(HIGHEST_TENTH_YEARLY_CHANGE_DOLLARS),
    "marketplace_premium_percent_rise": f"{MARKETPLACE_PREMIUM_PERCENT_RISE_2026}%",
    "marketplace_monthly_premium_2025": whole_dollars(MARKETPLACE_MONTHLY_PREMIUM_2025_DOLLARS),
    "marketplace_monthly_premium_2026": whole_dollars(MARKETPLACE_MONTHLY_PREMIUM_2026_DOLLARS),

    # Truce Sealed
    "mediator_breakthrough_day": month_and_day(MEDIATOR_BREAKTHROUGH_DAY),
    "iran_war_start_long": long_date(IRAN_WAR_START),
    "iran_war_us_deaths": str(IRAN_WAR_US_DEATHS),
    "iran_war_us_killed_or_wounded": str(IRAN_WAR_US_KILLED_OR_WOUNDED),
    "iran_war_cost_billions": f"{IRAN_WAR_COST_BILLIONS:.1f}",
    "gas_price_today": dollars_and_cents(GAS_PRICE_TODAY_DOLLARS),
    "gas_price_year_ago": dollars_and_cents(GAS_PRICE_YEAR_AGO_DOLLARS),
    "house_iran_war_resolutions_passed": count_in_words(HOUSE_IRAN_WAR_RESOLUTIONS_PASSED),
    "senate_iran_vote_june_23": vote_tally(SENATE_IRAN_VOTE_JUNE_23_YEAS, SENATE_IRAN_VOTE_JUNE_23_NAYS),
    "senate_iran_vote_september_24": vote_tally(SENATE_IRAN_VOTE_SEPTEMBER_24_YEAS, SENATE_IRAN_VOTE_SEPTEMBER_24_NAYS),
    "jcpoa_enrichment_cap": f"{JCPOA_ENRICHMENT_CAP_PERCENT}%",
    "jcpoa_stockpile_cap": f"{JCPOA_STOCKPILE_CAP_KILOGRAMS} kilograms",
}

# The PAGE_FIGURES worked out from other figures rather than read from a
# source. check.py works each one out again, and fails if one is typed into
# the template by hand.
DERIVED_FIGURE_NAMES = (
    "house_seats_for_veto_proof_majority",
    "senate_seats_for_veto_proof_majority",
    "senate_race_count",
    "months_since_four_to_five_weeks_remark",
    "iran_war_cost_billions",
    "gas_price_today",
    "gas_price_year_ago",
)
