#!/usr/bin/env python3
"""Generate Batch B1 practice x city location pages (SEO_PLAN.md Phase 3).

Builds 9 pages = {Fort Lauderdale, Hollywood, Hallandale Beach}
              x {Criminal Defense, DUI, Car Accident}.

Each page composes authored, city-specific and practice-specific content plus a
unique intro and FAQ set, so no two pages are find-and-replace clones. Structure
matches the Dania Beach exemplar (criminal-defense-lawyer-dania-beach.html).

Idempotent: rewrites the target files from the data below on each run.
"""
import html as _html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://hoffman.legal/"

# ---------------------------------------------------------------- city data ---
CITIES = {
    "fort-lauderdale": {
        "name": "Fort Lauderdale",
        "pd": "the Fort Lauderdale Police Department",
        "pd_note": (
            "Unlike some neighboring cities, Fort Lauderdale runs its own municipal "
            "police department, and its officers make most of the traffic stops and "
            "arrests downtown, along the beach, and on the highways that cut through the city."
        ),
        "courts": (
            "Fort Lauderdale is the seat of Broward County, so the <strong>Broward County "
            "Central Courthouse at 201 SE 6th Street</strong> — where felony cases and first "
            "appearances are handled — is right downtown. County and traffic matters are heard "
            "in the same 17th Judicial Circuit, and the Broward State Attorney's Office, "
            "headquartered here, prosecutes the charges."
        ),
        "corridors_intro": (
            "As the busiest city in Broward, Fort Lauderdale concentrates enforcement and "
            "collisions along a handful of heavily traveled corridors:"
        ),
        "corridors": [
            "<strong>I-95</strong> — including the stretch known as one of the deadliest miles in the state, between the I-595 interchange and Marina Mile Boulevard.",
            "<strong>US-1 (Federal Highway)</strong> — dense with intersections and pedestrians, especially between Sunrise Boulevard and SE 17th Street.",
            "<strong>Broward Boulevard, Sunrise Boulevard, and Oakland Park Boulevard</strong> — high-volume east-west arteries with frequent signalized crashes.",
            "<strong>Las Olas Boulevard and the beach district</strong> — heavy foot traffic, nightlife, and tourists, where pedestrian, bicycle, and DUI incidents cluster.",
        ],
        "hospital": "Broward Health Medical Center, a Level I trauma center on the north side of downtown",
        "landmarks": "Las Olas Boulevard, the beach, Port Everglades, and the downtown entertainment district",
    },
    "hollywood-fl": {
        "name": "Hollywood",
        "pd": "the Hollywood Police Department",
        "pd_note": (
            "Hollywood operates its own police department rather than contracting with the "
            "county, so Hollywood officers handle the stops, DUI investigations, and arrests "
            "you may be facing — from the beach Broadwalk to the SR-7 corridor."
        ),
        "courts": (
            "Hollywood is home to the <strong>Broward South Regional Courthouse at 3550 "
            "Hollywood Boulevard</strong>, where misdemeanor, traffic, and county cases from "
            "the south end of the county are heard. Felony matters move to the Central "
            "Courthouse in Fort Lauderdale, and both sit within the 17th Judicial Circuit."
        ),
        "corridors_intro": (
            "Hollywood's crashes and enforcement stops cluster on a few well-known roads, "
            "several of them kept busy around the clock by the casino and beach traffic:"
        ),
        "corridors": [
            "<strong>State Road 7 (US-441) at Sheridan Street</strong> — one of the city's highest-crash intersections, kept busy 24/7 by the nearby Seminole Hard Rock Hotel &amp; Casino.",
            "<strong>State Road 7 and Hollywood Boulevard</strong> — heavy transit and commercial traffic and a persistent crash hotspot.",
            "<strong>US-1 (Federal Highway) and Sheridan Street</strong> — busy corridors with frequent rear-end and turning collisions.",
            "<strong>Hollywood Beach and the Broadwalk area</strong> — pedestrians, cyclists, and nightlife where DUI and disorderly-conduct allegations are common on weekends.",
        ],
        "hospital": "Memorial Regional Hospital, one of Florida's Level I trauma centers, at 3501 Johnson Street",
        "landmarks": "Hollywood Beach, the Broadwalk, ArtsPark at Young Circle, and the Seminole Hard Rock",
    },
    "hallandale-beach": {
        "name": "Hallandale Beach",
        "pd": "the Hallandale Beach Police Department",
        "pd_note": (
            "Hallandale Beach has its own police department, headquartered at 400 South Federal "
            "Highway, and its officers patrol the dense US-1 corridor and the casino and beach "
            "areas where much of the city's activity happens."
        ),
        "courts": (
            "Hallandale Beach sits at the southern edge of Broward County. Misdemeanor and "
            "traffic cases are generally heard at the <strong>Broward South Regional Courthouse "
            "at 3550 Hollywood Boulevard</strong>, just to the north, while felonies go to the "
            "Central Courthouse in Fort Lauderdale — all within Florida's 17th Judicial Circuit."
        ),
        "corridors_intro": (
            "For a compact city, Hallandale Beach carries heavy through-traffic, and incidents "
            "concentrate on its main corridors and destinations:"
        ),
        "corridors": [
            "<strong>US-1 (Federal Highway)</strong> — one of the most crash-prone corridors in Broward, with constant driveways, mid-block crossings, and cars entering and exiting commercial lots.",
            "<strong>Hallandale Beach Boulevard</strong> — a busy east-west route with rear-end collisions at its signalized intersections.",
            "<strong>Gulfstream Park and The Village at Gulfstream</strong> — racing, casino, dining, and shopping traffic that spikes on evenings and weekends.",
            "<strong>The beach and A1A area</strong> — pedestrian-heavy zones near the coast where distracted-driving crashes occur.",
        ],
        "hospital": "Memorial Regional Hospital in Hollywood and Aventura Hospital just to the south",
        "landmarks": "Gulfstream Park, The Village at Gulfstream, and the beach",
    },
}

# ------------------------------------------------------------ practice data ---
PRACTICES = {
    "criminal-defense": {
        "label": "Criminal Defense",
        "prefix": "criminal-defense-lawyer",
        "hub": "criminal-defense.html",
        "hub_label": "Criminal Defense",
        "service_type": "Criminal Defense",
        "kind": "criminal",
        "title": "{city} Criminal Defense Lawyer | Broward County, FL | Hoffman Legal",
        "h1": "{city} Criminal Defense Lawyer",
        "desc": (
            "Charged with a crime in {city}? Local criminal defense lawyer and former public "
            "defender David Hoffman handles Broward cases from arrest through trial. Free 24/7 "
            "consultation: (954) 459-4236."
        ),
        "kicker": "Criminal Defense in {city}",
        "substant_h2": "How We Defend {city} Criminal Cases",
        "substant": (
            "<p>Every criminal case turns on details: whether police had a lawful reason to stop "
            "or detain you, whether a search was valid, how evidence was gathered and stored, and "
            "how the State chooses to charge. Attorney David Hoffman, a former public defender, "
            "reads that record the way a prosecutor would — looking for the weak points before "
            "they become your problem.</p>"
            "<p>From misdemeanors to serious felonies, the goal is the same: understand exactly "
            "what you are facing, protect your rights at every stage, and pursue the outcome that "
            "does the least damage to your record, your freedom, and your future — whether that is "
            "a dismissal, a diversion program that keeps a conviction off your record, a favorable "
            "plea, or trial.</p>"
            "<p>Just as important is how you are treated along the way. You should understand your "
            "options in plain language, know what each decision means, and be able to reach your "
            "lawyer when something changes. At Hoffman Legal you work directly with attorney David "
            "Hoffman, who will tell you honestly what to expect rather than what you want to hear, "
            "and build a strategy around the specific facts of your {city} case.</p>"
        ),
        "charges": [
            ("DUI Defense", "dui-defense.html"),
            ("Drug Possession", "drug-possession-cases.html"),
            ("Theft, Robbery &amp; Burglary", "theft-robbery-burglary.html"),
            ("Assault &amp; Battery", "assault-battery.html"),
            ("Sexual Battery Cases", "sexual-battery-cases.html"),
            ("White Collar Crimes", "white-collar-crimes.html"),
            ("Injunctions", "injunctions.html"),
            ("Expunge &amp; Seal Records", "expunge-seal-records.html"),
            ("Early Termination of Probation", "early-termination-of-probation.html"),
        ],
        "consequences_h2": "What a {city} Conviction Can Cost You",
        "consequences": (
            "<p>In {city}, as everywhere in Florida, the sentence a judge imposes is only part of "
            "the story. A criminal conviction can follow you for years — affecting employment and "
            "professional licenses, housing applications, a security clearance, financial aid, "
            "immigration status, and your right to possess a firearm. Even a plea that feels "
            "convenient in the moment, or a withhold of adjudication, can carry collateral "
            "consequences that are difficult to undo later.</p>"
            "<p>That is exactly why it is worth understanding the full weight of what is at stake "
            "before you make any decision. A short, free consultation can make clear what you are "
            "actually facing, what defenses may exist, and whether a path exists to protect your "
            "record — often before the first court date in {city} even arrives.</p>"
        ),
        "charges_h2": "Charges We Defend in {city}",
        "steps_h2": "What to Do After an Arrest in {city}",
        "steps": [
            "<strong>Stay silent about the incident.</strong> Be polite, but do not explain or argue. You have the right to remain silent — use it.",
            "<strong>Do not consent to searches</strong> of your car, phone, or home until you have spoken with a lawyer.",
            "<strong>Write down what you remember</strong> while it is fresh: the location, the stated reason for the stop, what was said, and any witnesses.",
            "<strong>Call a lawyer before your first appearance,</strong> which in Broward usually happens within 24 hours and sets bond and release conditions.",
            "<strong>Do not discuss the case</strong> on recorded jail calls, with friends, or on social media.",
        ],
    },
    "dui": {
        "label": "DUI Defense",
        "prefix": "dui-lawyer",
        "hub": "dui-defense.html",
        "hub_label": "DUI Defense",
        "service_type": "DUI Defense",
        "kind": "criminal",
        "title": "{city} DUI Lawyer | DUI Defense Attorney | Broward County | Hoffman Legal",
        "h1": "{city} DUI Lawyer",
        "desc": (
            "Arrested for DUI in {city}? Local DUI defense lawyer David Hoffman challenges the "
            "stop, the field sobriety exercises, and the breath test. Free 24/7 consultation: "
            "(954) 459-4236."
        ),
        "kicker": "DUI Defense in {city}",
        "substant_h2": "Fighting a {city} DUI Charge",
        "substant": (
            "<p>A DUI is not a foregone conclusion just because you were arrested. These cases are "
            "built on procedure, and procedure can break down. Was there a lawful reason for the "
            "stop? Were the field sobriety exercises administered and scored correctly? Was the "
            "breath instrument properly maintained and operated, and was the 20-minute observation "
            "period actually observed? Each answer can change the strength of the State's case.</p>"
            "<p>A DUI also runs on two tracks at once — the criminal case in court and an "
            "administrative action against your license through the DHSMV, which has strict early "
            "deadlines. Attorney David Hoffman addresses both, works to protect your ability to "
            "drive, and looks for every issue in the stop, the testing, and the reports that can "
            "be used in your defense.</p>"
            "<p>Many people assume a DUI arrest means an automatic conviction, but that is simply "
            "not true. Breath readings can be unreliable, medical conditions and nerves can mimic "
            "impairment on roadside exercises, and officers do not always follow the required "
            "procedures. The sooner your {city} case is reviewed, the more can be done — from "
            "preserving evidence to protecting your license and negotiating from a position of "
            "strength.</p>"
        ),
        "charges": [
            ("First-Offense DUI", "dui-defense.html"),
            ("Breath &amp; Blood Test Issues", "dui-defense.html"),
            ("License Suspension", "dui-defense.html"),
            ("Drug Possession", "drug-possession-cases.html"),
            ("Criminal Defense", "criminal-defense.html"),
            ("Expunge &amp; Seal Records", "expunge-seal-records.html"),
        ],
        "consequences_h2": "The Stakes of a {city} DUI Conviction",
        "consequences": (
            "<p>A Florida DUI conviction carries consequences that reach well beyond {city}. Even a "
            "first offense can mean fines, probation, community service, mandatory DUI school, "
            "vehicle impoundment, and a license suspension — and the conviction cannot be sealed or "
            "expunged, so it stays on your record permanently. Insurance costs typically climb, and "
            "a commercial driver or professional can face added career consequences.</p>"
            "<p>Because the penalties escalate quickly with prior offenses, a high breath reading, "
            "an accident, or a minor in the vehicle, the decisions you make early in a {city} DUI "
            "case matter. Understanding your options — and the weaknesses in the State's evidence — "
            "before you decide how to proceed can change the outcome significantly. A conviction "
            "can also affect your job, especially if you drive for a living, so it is worth taking "
            "the charge seriously from day one.</p>"
        ),
        "charges_h2": "{city} DUI Issues We Handle",
        "steps_h2": "What to Do After a {city} DUI Arrest",
        "steps": [
            "<strong>Act fast on your license.</strong> You generally have only 10 days to address the administrative suspension of your driving privilege.",
            "<strong>Stay silent beyond identifying yourself.</strong> You do not have to answer questions about where you were or what you drank.",
            "<strong>Write down the details</strong> of the stop, the exercises you were asked to perform, and the timeline while they are fresh.",
            "<strong>Preserve evidence.</strong> Note any medical conditions, footwear, or road and weather conditions that could explain the officer's observations.",
            "<strong>Call a DUI lawyer before making decisions</strong> about pleas, testing, or statements to anyone about the case.",
        ],
    },
    "car-accident": {
        "label": "Car Accident",
        "prefix": "car-accident-lawyer",
        "hub": "car-accidents.html",
        "hub_label": "Car Accidents",
        "service_type": "Personal Injury — Car Accidents",
        "kind": "injury",
        "title": "{city} Car Accident Lawyer | Personal Injury Attorney | Hoffman Legal",
        "h1": "{city} Car Accident Lawyer",
        "desc": (
            "Injured in a {city} car accident? Personal injury lawyer David Hoffman handles "
            "insurance claims, PIP, and injury lawsuits so you can focus on recovery. Free "
            "consultation: (954) 459-4236."
        ),
        "kicker": "Car Accident &amp; Injury Help in {city}",
        "substant_h2": "After a {city} Crash: Protecting Your Claim",
        "substant": (
            "<p>Florida is a no-fault state, so after a {city} crash your own Personal Injury "
            "Protection (PIP) coverage usually pays first — but only up to a limit, and only if "
            "you seek treatment within the state's 14-day window. When injuries are serious, you "
            "may be able to step outside no-fault and pursue the at-fault driver directly. Getting "
            "these steps right early protects what your claim is ultimately worth.</p>"
            "<p>Insurers move quickly to limit what they pay, and a recorded statement or a fast "
            "lowball offer can cost you. Hoffman Legal deals with the adjusters, documents your "
            "injuries and losses, and pursues fair compensation for medical bills, lost wages, and "
            "pain and suffering — so you can focus on recovering, not fighting the insurance company.</p>"
            "<p>Every {city} crash is different — a rear-end collision on a busy corridor, a "
            "distracted-driving wreck at an intersection, a hit-and-run, or a serious highway "
            "crash. What they share is that the strength of your claim is often decided in the "
            "first weeks, through prompt treatment and careful documentation. Getting a lawyer "
            "involved early helps make sure nothing that supports your recovery is lost.</p>"
        ),
        "charges": [
            ("Personal Injury", "personal-injury.html"),
            ("Car Accidents", "car-accidents.html"),
            ("Truck Accidents", "truck-accidents.html"),
            ("Motorcycle Accidents", "motorcycle-accidents.html"),
            ("Pedestrian Accidents", "pedestrian-accidents.html"),
            ("Rideshare Accidents", "rideshare-accidents.html"),
            ("Wrongful Death", "wrongful-death.html"),
        ],
        "consequences_h2": "What Your {city} Injury Claim Can Include",
        "consequences": (
            "<p>When someone else's negligence causes a {city} crash, Florida law allows you to "
            "recover more than just a repair bill. Depending on your injuries and available "
            "coverage, a claim can include past and future medical expenses, lost wages and lost "
            "earning capacity, the cost of rehabilitation and care, property damage, and "
            "compensation for pain, suffering, and the disruption to your life.</p>"
            "<p>The value of a claim depends on getting the details right — prompt medical "
            "treatment, thorough documentation, and a clear link between the crash and your "
            "injuries. Waiting too long or handling the insurer alone can quietly reduce what you "
            "receive, which is why it helps to have Hoffman Legal involved early in your {city} "
            "case. There is also a deadline: Florida limits how long you have to bring an injury "
            "claim, so it is best not to wait to learn where you stand.</p>"
        ),
        "charges_h2": "{city} Injury Cases We Handle",
        "steps_h2": "What to Do After a Car Accident in {city}",
        "steps": [
            "<strong>Call the police and get a crash report.</strong> An official report is important documentation for any later claim.",
            "<strong>Get medical care within 14 days.</strong> Florida PIP requires prompt treatment, and early records connect your injuries to the crash.",
            "<strong>Document everything</strong> — photos of the scene and vehicles, the other driver's information, and the names of any witnesses.",
            "<strong>Do not give a recorded statement</strong> to the other driver's insurer or accept a quick settlement before speaking with a lawyer.",
            "<strong>Keep records</strong> of medical visits, time missed from work, and out-of-pocket costs related to the crash.",
        ],
    },
}

# --------------------------------------------------- per-page unique content ---
# (city_key, practice_key): {intro, faqs:[(q,a)...]}
PAGES = {
    ("fort-lauderdale", "criminal-defense"): {
        "intro": (
            "An arrest in Fort Lauderdale means your case runs through the busiest courts and the "
            "largest prosecutor's office in Broward County — often just blocks from where it "
            "started. Attorney David Hoffman, a former public defender based nearby in Dania Beach, "
            "defends people charged with crimes in Fort Lauderdale and knows how these downtown "
            "courtrooms and the Fort Lauderdale Police Department operate."
        ),
        "faqs": [
            ("Where will my Fort Lauderdale criminal case be heard?",
             "Felony cases and first appearances are handled at the Broward County Central Courthouse at 201 SE 6th Street in downtown Fort Lauderdale. Misdemeanor and traffic matters are heard in the same 17th Judicial Circuit, and the Broward State Attorney's Office prosecutes the charges."),
            ("Who makes arrests in Fort Lauderdale?",
             "Fort Lauderdale has its own municipal police department. Its officers make most stops and arrests within the city, though the Broward Sheriff's Office and state agencies also operate in the area. After arrest, most people are booked into the BSO Main Jail on SE 1st Avenue."),
            ("Should I talk to detectives before hiring a lawyer?",
             "No. Politely decline to answer questions about the incident and ask for a lawyer. Statements to Fort Lauderdale police can be used against you, and you have the right to remain silent. Call Hoffman Legal at (954) 459-4236 first."),
            ("Can a first-time charge be kept off my record?",
             "Sometimes. Depending on the charge and your history, options like a diversion program or a withhold of adjudication may help you avoid a conviction, and some records can later be sealed or expunged. An early consultation is the best way to learn what applies."),
            ("Do you offer free consultations in Fort Lauderdale?",
             "Yes. Every initial consultation with attorney David Hoffman is free and confidential, and he is available 24/7. The office is a short drive south in Dania Beach."),
        ],
    },
    ("fort-lauderdale", "dui"): {
        "intro": (
            "Fort Lauderdale's nightlife, beaches, and highways make it one of the most active DUI "
            "enforcement areas in Broward County. If you were arrested on I-95, along Federal "
            "Highway, or near Las Olas and the beach, attorney David Hoffman examines every step of "
            "the stop and the testing to build your defense."
        ),
        "faqs": [
            ("What happens to my license after a Fort Lauderdale DUI?",
             "A DUI arrest triggers an administrative suspension separate from the criminal case. You generally have only 10 days to challenge it or apply for a hardship license, which is why calling a lawyer immediately matters."),
            ("Where is my Fort Lauderdale DUI case heard?",
             "DUI is typically a misdemeanor heard within the 17th Judicial Circuit; Fort Lauderdale cases move through the county courts downtown. If aggravating factors elevate the charge, it may be handled at the Central Courthouse on SE 6th Street."),
            ("Can the breath test result be challenged?",
             "Often, yes. Breath instruments must be properly maintained and operated, the officer must complete a 20-minute observation period, and the exercises must be administered correctly. Any breakdown can undermine the State's case."),
            ("Do I have to perform field sobriety exercises?",
             "Field sobriety exercises are voluntary, and refusing them is different from refusing a lawful breath test. How the exercises were requested and scored is frequently a defense issue in Fort Lauderdale DUI cases."),
            ("Is the consultation free?",
             "Yes. David Hoffman offers a free, confidential DUI consultation and is available 24/7 at (954) 459-4236."),
        ],
    },
    ("fort-lauderdale", "car-accident"): {
        "intro": (
            "Fort Lauderdale's heavy corridors — I-95, Federal Highway, Broward and Sunrise "
            "Boulevards — produce some of Broward County's most serious crashes. If you were hurt "
            "in a Fort Lauderdale accident, Hoffman Legal handles the insurance side so you can "
            "focus on getting better."
        ),
        "faqs": [
            ("Which roads see the most Fort Lauderdale crashes?",
             "I-95 — including a stretch between the I-595 interchange and Marina Mile Boulevard long cited as one of the state's deadliest — plus US-1 between Sunrise Boulevard and SE 17th Street, and the Las Olas and beach districts with heavy pedestrian traffic."),
            ("Where should I seek treatment after a crash?",
             "Get medical care promptly. Broward Health Medical Center is a Level I trauma center in Fort Lauderdale for serious injuries. Under Florida PIP, treatment within 14 days is important to preserve your claim."),
            ("Does Florida no-fault limit what I can recover?",
             "Your own PIP pays first, up to its limit. When injuries are serious, you may be able to pursue the at-fault driver for additional damages, including pain and suffering. A lawyer can assess whether your case qualifies."),
            ("Should I talk to the other driver's insurer?",
             "Not before speaking with a lawyer. Recorded statements and quick settlement offers often work against you. Let Hoffman Legal handle the adjusters."),
            ("What does a consultation cost?",
             "Nothing. Car accident consultations are free, and injury cases are typically handled on a contingency basis — call (954) 459-4236."),
        ],
    },
    ("hollywood-fl", "criminal-defense"): {
        "intro": (
            "If you were arrested in Hollywood, your case likely begins with the Hollywood Police "
            "Department and heads to the South Regional Courthouse right on Hollywood Boulevard. "
            "Attorney David Hoffman, a former public defender based minutes away in Dania Beach, "
            "defends Hollywood clients and knows these local courts well."
        ),
        "faqs": [
            ("Which courthouse handles Hollywood criminal cases?",
             "Misdemeanor and traffic cases from Hollywood are generally heard at the Broward South Regional Courthouse at 3550 Hollywood Boulevard, while felonies go to the Central Courthouse in Fort Lauderdale. Both are part of the 17th Judicial Circuit."),
            ("Who arrests people in Hollywood?",
             "Hollywood has its own police department, so Hollywood officers handle most stops and arrests in the city. After arrest, people are typically booked into the BSO Main Jail in Fort Lauderdale, and the Broward State Attorney prosecutes."),
            ("What areas of Hollywood see the most arrests?",
             "Enforcement is heavy along State Road 7 near the Seminole Hard Rock, on Hollywood Boulevard, on US-1, and around the beach and Broadwalk, especially on nights and weekends."),
            ("Should I answer police questions first?",
             "No. Remain silent about the incident and ask for a lawyer before answering questions or consenting to a search. Call Hoffman Legal at (954) 459-4236."),
            ("Do you offer free consultations for Hollywood cases?",
             "Yes — every consultation is free and confidential, and attorney David Hoffman is available 24/7."),
        ],
    },
    ("hollywood-fl", "dui"): {
        "intro": (
            "With the Seminole Hard Rock, the beach Broadwalk, and busy corridors like SR-7 and "
            "US-1, Hollywood is a frequent site of DUI stops. If Hollywood police arrested you for "
            "DUI, attorney David Hoffman reviews the stop, the exercises, and the breath testing "
            "for every possible defense."
        ),
        "faqs": [
            ("How quickly do I need to act on my license after a Hollywood DUI?",
             "Very quickly — generally within 10 days of the arrest to challenge the administrative suspension or seek a hardship license. This deadline is separate from your criminal court date."),
            ("Where will my Hollywood DUI case be heard?",
             "Most DUI cases are misdemeanors heard within the 17th Judicial Circuit, with Hollywood cases moving through the county courts, including matters at the South Regional Courthouse on Hollywood Boulevard."),
            ("Does being near the casino affect my case?",
             "The area around the Seminole Hard Rock and SR-7 sees heavy patrols and traffic. Where and why you were stopped still has to meet legal standards, and that is often where a defense begins."),
            ("Can I refuse the breath test?",
             "You can, but refusing a lawful breath test carries its own license consequences. Whether the request and testing were proper is a separate question a DUI lawyer will examine."),
            ("Is the DUI consultation free?",
             "Yes. Call (954) 459-4236 for a free, confidential consultation, available 24/7."),
        ],
    },
    ("hollywood-fl", "car-accident"): {
        "intro": (
            "Hollywood's busiest roads — State Road 7 at Sheridan Street, Hollywood Boulevard, and "
            "US-1 — are also its most crash-prone, kept busy by casino, transit, and beach traffic. "
            "If you were injured in a Hollywood crash, Hoffman Legal handles the claim so you can "
            "focus on recovery."
        ),
        "faqs": [
            ("Which Hollywood intersections are most dangerous?",
             "State Road 7 (US-441) at Sheridan Street is among the city's highest-crash intersections, kept busy around the clock by the nearby Seminole Hard Rock. State Road 7 at Hollywood Boulevard and the US-1 corridor also see frequent collisions."),
            ("Where can I get trauma care after a Hollywood crash?",
             "Memorial Regional Hospital at 3501 Johnson Street is a Level I trauma center in Hollywood, equipped for the most serious injuries. Seek treatment within 14 days to protect your PIP claim."),
            ("How does Florida no-fault apply to my crash?",
             "Your PIP coverage pays first up to its limit. If your injuries are serious, you may be able to pursue the at-fault driver for additional compensation, including pain and suffering."),
            ("Should I accept the insurer's first offer?",
             "No. Early offers are often low. Speak with Hoffman Legal before signing anything or giving a recorded statement."),
            ("What will a consultation cost me?",
             "Nothing. Car accident consultations are free and injury cases are typically handled on contingency — call (954) 459-4236."),
        ],
    },
    ("hallandale-beach", "criminal-defense"): {
        "intro": (
            "A Hallandale Beach arrest usually starts with the city's own police department and "
            "moves north into the Broward court system. Attorney David Hoffman, a former public "
            "defender based nearby in Dania Beach, defends Hallandale Beach clients and understands "
            "how these cases are charged and resolved."
        ),
        "faqs": [
            ("Where are Hallandale Beach criminal cases heard?",
             "Misdemeanor and traffic cases are generally heard at the Broward South Regional Courthouse at 3550 Hollywood Boulevard, just north of the city, while felonies go to the Central Courthouse in Fort Lauderdale — all in the 17th Judicial Circuit."),
            ("Who handles policing in Hallandale Beach?",
             "Hallandale Beach has its own police department, headquartered at 400 South Federal Highway. Its officers make most local stops and arrests, and cases are prosecuted by the Broward State Attorney's Office."),
            ("Where does enforcement concentrate in Hallandale Beach?",
             "Along the US-1 (Federal Highway) corridor, on Hallandale Beach Boulevard, and around Gulfstream Park and the beach — areas with heavy traffic and nightlife."),
            ("Should I speak to police before calling a lawyer?",
             "No. Stay silent about the incident, decline searches, and ask for a lawyer. Call Hoffman Legal at (954) 459-4236 before answering questions."),
            ("Are consultations free?",
             "Yes. Every consultation with attorney David Hoffman is free, confidential, and available 24/7."),
        ],
    },
    ("hallandale-beach", "dui"): {
        "intro": (
            "The dense Federal Highway corridor and the crowds around Gulfstream Park and the beach "
            "make Hallandale Beach a common place for DUI stops. If the Hallandale Beach Police "
            "arrested you, attorney David Hoffman examines the stop, the field exercises, and the "
            "breath test for weaknesses."
        ),
        "faqs": [
            ("What is the deadline to protect my license after a Hallandale Beach DUI?",
             "Generally 10 days from the arrest to challenge the administrative suspension or request a hardship license. This is separate from, and earlier than, your criminal court date."),
            ("Which court handles my Hallandale Beach DUI?",
             "Most DUI cases are misdemeanors within the 17th Judicial Circuit and are heard in the Broward county courts, including matters at the South Regional Courthouse in nearby Hollywood."),
            ("Do casino and beach crowds affect DUI stops here?",
             "The US-1 corridor and the areas near Gulfstream Park and the beach draw heavy patrols. Even so, the stop and the testing must meet legal standards — the starting point of many defenses."),
            ("Should I perform the roadside exercises?",
             "Field sobriety exercises are voluntary. How they were requested, demonstrated, and scored is frequently challenged in Hallandale Beach DUI cases."),
            ("Is the consultation really free?",
             "Yes. Call (954) 459-4236 any time for a free, confidential DUI consultation."),
        ],
    },
    ("hallandale-beach", "car-accident"): {
        "intro": (
            "US-1 through Hallandale Beach is one of Broward's most crash-prone corridors, with "
            "constant driveways, crossings, and casino and beach traffic. If you were injured in a "
            "Hallandale Beach crash, Hoffman Legal handles the insurance fight for you."
        ),
        "faqs": [
            ("Why is US-1 through Hallandale Beach so crash-prone?",
             "Federal Highway here is dense with driveways, mid-block pedestrian crossings, and cars entering and exiting commercial lots, which drives frequent rear-end and turning collisions — especially near Gulfstream Park and the beach."),
            ("Where should I get treated after a crash?",
             "Seek care promptly. Memorial Regional Hospital in Hollywood and Aventura Hospital just to the south handle serious injuries. Treatment within 14 days protects your Florida PIP claim."),
            ("How much can I recover after a Hallandale Beach crash?",
             "PIP pays first up to its limit. If injuries are serious, you may be able to pursue the at-fault driver for additional damages, including pain and suffering. A lawyer can evaluate your options."),
            ("Should I deal with the insurer myself?",
             "It is better not to. Adjusters aim to limit payouts, and a recorded statement can hurt your claim. Let Hoffman Legal handle communications."),
            ("What does it cost to talk to a lawyer?",
             "Nothing up front. Consultations are free and injury cases are typically handled on contingency — call (954) 459-4236."),
        ],
    },
}

ADDR = {
    "streetAddress": "101 SW 1st Street, Suite CW12",
    "addressLocality": "Dania Beach",
    "addressRegion": "FL",
    "postalCode": "33004",
    "addressCountry": "US",
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def strip_tags(s):
    return _html.unescape(re.sub(r"<[^>]+>", "", s))


def build(city_key, prac_key):
    city = CITIES[city_key]
    prac = PRACTICES[prac_key]
    page = PAGES[(city_key, prac_key)]
    cname = city["name"]
    slug = f"{prac['prefix']}-{city_key}.html"
    url = BASE + slug

    def f(t):
        return t.replace("{city}", cname)

    title = f(prac["title"])
    desc = f(prac["desc"])

    # nearby: other two B1 cities, same practice
    nearby = []
    for ck in CITIES:
        if ck != city_key:
            nearby.append((CITIES[ck]["name"], f"{prac['prefix']}-{ck}.html"))

    # ---- schema ----
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": "Areas We Serve", "item": BASE + "locations.html"},
            {"@type": "ListItem", "position": 3, "name": f"{cname} {prac['label']}", "item": url},
        ],
    }
    legalservice = {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "@id": url + "#service",
        "name": f"Hoffman Legal — {cname} {prac['label']}",
        "url": url,
        "parentOrganization": {"@id": BASE + "#legalservice"},
        "telephone": "+1-954-459-4236",
        "email": "david@hoffman.legal",
        "image": BASE + "dhh-headshot.jpg",
        "priceRange": "$$",
        "address": dict({"@type": "PostalAddress"}, **ADDR),
        "areaServed": {
            "@type": "City",
            "name": cname,
            "containedInPlace": {"@type": "AdministrativeArea", "name": "Broward County, Florida"},
        },
        "serviceType": prac["service_type"],
        "provider": {"@id": BASE + "#attorney"},
    }
    faqpage = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in page["faqs"]
        ],
    }

    def jsonld(obj, tag):
        body = json.dumps(obj, indent=2, ensure_ascii=False)
        body = "\n".join("  " + ln for ln in body.splitlines())
        return f'  <script type="application/ld+json" data-jsonld="{tag}">\n{body}\n  </script>'

    # ---- body sections ----
    corridors = "\n".join(f"        <li>{c}</li>" for c in city["corridors"])
    charges = "\n".join(
        f'        <a href="{u}">{lbl}</a>' for lbl, u in prac["charges"]
    )
    steps = "\n".join(f"        <li>{s}</li>" for s in prac["steps"])
    faqs_html = "\n".join(
        f'      <div class="faq-item">\n        <h3>{esc(q)}</h3>\n        <p>{a}</p>\n      </div>'
        for q, a in page["faqs"]
    )
    nearby_html = "\n".join(
        f'        <a href="{u}">{n}</a>' for n, u in nearby
    )

    if prac["kind"] == "injury":
        heard_h2 = f"Where {cname} Crashes Happen"
        heard_lead = city["corridors_intro"]
        heard_extra = (
            f"After a {cname} crash, an official police report and prompt medical records become "
            f"the backbone of any claim. Florida's no-fault system and its 14-day treatment window "
            f"make the first days after a collision especially important, and {city['hospital']} "
            f"handles the most serious injuries in this area."
        )
        local_h2 = f"Local Injury Help in {cname}"
        local_p = (
            f"<p>A serious crash in {cname} upends everything — your health, your income, and "
            f"your peace of mind — while the at-fault driver's insurer works to pay as little as "
            f"possible. Hoffman Legal, based nearby in Dania Beach, levels that fight for injured "
            f"people across South Broward.</p>"
            f"<p>You should not have to negotiate with an adjuster while you are still recovering. "
            f"Attorney David Hoffman handles the insurance company directly, so you can focus on "
            f"healing and getting your life back on track after a {cname} crash.</p>"
            f"<p>{city['pd_note']}</p>"
        )
        why_local = (
            f"<p>Insurance companies count on injured people handling claims alone. A {cname} "
            f"claim runs through Florida's no-fault rules, PIP deadlines, and — when injuries are "
            f"serious — the path to holding the at-fault driver accountable. A local lawyer who "
            f"knows the Broward courts and the roads where these crashes happen can document the "
            f"case properly and push back when an adjuster undervalues it. Because Hoffman Legal is "
            f"based nearby in Dania Beach, you work directly with the attorney handling your "
            f"matter — not a call center.</p>"
        )
    else:
        heard_h2 = f"Where {cname} Cases Are Heard"
        heard_lead = city["courts"]
        heard_extra = (
            f"After a {cname} arrest, most people are booked into the Broward Sheriff's Office "
            f"Main Jail at 555 SE 1st Avenue in Fort Lauderdale and are brought before a judge for "
            f"a first appearance within 24 hours, where bond and conditions of release are set. "
            f"Having a lawyer involved at that early stage can make a real difference."
        )
        local_h2 = f"Local Defense in {cname}"
        local_p = (
            f"<p>A criminal charge in {cname} can put your job, your record, your license, and "
            f"your family under real pressure, and the system is built so that power skews toward "
            f"the state. Hoffman Legal exists to level that fight — with honest advice and a "
            f"defense built around the facts of your case.</p>"
            f"<p>{city['pd_note']}</p>"
        )
        why_local = (
            f"<p>Two lawyers can read the same statute and reach different results, because so "
            f"much of a case turns on people and process. A {cname} case moves through the Broward "
            f"State Attorney's Office and the 17th Judicial Circuit, each with its own diversion "
            f"programs, filing practices, and expectations at plea and sentencing. An attorney who "
            f"works in these courts regularly understands how a charge tends to be handled locally "
            f"and where there is room to negotiate. Being based nearby in Dania Beach also means "
            f"you can meet in person and reach someone quickly when something changes.</p>"
        )

    page_html = TEMPLATE.format(
        title=title,
        desc=desc,
        url=url,
        breadcrumb=jsonld(breadcrumb, "breadcrumb"),
        legalservice=jsonld(legalservice, "legal-service"),
        faqpage=jsonld(faqpage, "faq"),
        crumb_label=f"{cname} {prac['label']}",
        kicker=f(prac["kicker"]),
        h1=f(prac["h1"]),
        intro=page["intro"],
        local_h2=local_h2,
        local_p=local_p,
        heard_h2=heard_h2,
        heard_lead=heard_lead,
        heard_extra=heard_extra,
        why_local=why_local,
        corridors_intro=city["corridors_intro"],
        corridors=corridors,
        substant_h2=f(prac["substant_h2"]),
        substant=f(prac["substant"]),
        consequences_h2=f(prac["consequences_h2"]),
        consequences=f(prac["consequences"]),
        charges_h2=f(prac["charges_h2"]),
        charges=charges,
        steps_h2=f(prac["steps_h2"]),
        steps=steps,
        faqs=faqs_html,
        faq_h2=f"{cname} {prac['label']} FAQ",
        nearby=nearby_html,
        hub=prac["hub"],
        hub_label=prac["hub_label"],
        cta_h2=(f"Injured in {cname}? Talk to Us Today."
                if prac["kind"] == "injury"
                else f"Charged in {cname}? Call Now."),
    )
    (ROOT / slug).write_text(page_html, encoding="utf-8")

    words = len(strip_tags(page_html[page_html.find("<body"):]).split())
    return slug, words


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-50SJMTCXDQ"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-50SJMTCXDQ');
  </script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="Hoffman Legal">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="robots" content="index,follow">
{breadcrumb}
{legalservice}
{faqpage}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700;900&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --background: hsl(222, 47%, 11%); --foreground: hsl(210, 40%, 98%);
      --card: hsl(217, 33%, 17%); --primary: hsl(40, 52%, 55%);
      --primary-foreground: hsl(222, 47%, 11%); --muted-foreground: hsl(215, 20%, 65%);
      --border: hsl(217, 33%, 22%); --rose-gold: #C5A47E;
      --font-serif: 'Playfair Display', Georgia, serif; --font-sans: 'Lato', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{ font-family: var(--font-sans); background: var(--background); color: var(--foreground); line-height: 1.7; -webkit-font-smoothing: antialiased; min-height: 100vh; display: flex; flex-direction: column; }}
    a {{ color: var(--primary); text-decoration: none; transition: color 0.2s; }}
    a:hover {{ color: var(--foreground); }}
    h1, h2, h3, h4 {{ font-family: var(--font-serif); font-weight: 600; }}
    .legal-header {{ background: rgba(17, 24, 39, 0.95); border-bottom: 1px solid rgba(191, 155, 107, 0.2); padding: 1.5rem 2rem; }}
    .legal-header-inner {{ max-width: 1152px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }}
    .logo {{ display: flex; align-items: center; gap: 0.625rem; }}
    .logo-box {{ width: 40px; height: 40px; border: 1.5px solid var(--rose-gold); display: flex; align-items: center; justify-content: center; }}
    .logo-letter {{ font-family: var(--font-serif); font-size: 1.5rem; color: var(--rose-gold); }}
    .logo-title {{ font-size: 0.8rem; letter-spacing: 0.25em; text-transform: uppercase; color: var(--rose-gold); }}
    .back-link {{ font-size: 0.8rem; letter-spacing: 0.1em; text-transform: uppercase; font-weight: 700; }}
    .crumb {{ max-width: 1000px; margin: 0 auto; padding: 1.25rem 1.5rem 0; font-size: 0.8rem; letter-spacing: 0.05em; color: var(--muted-foreground); }}
    .crumb a {{ color: var(--muted-foreground); }}
    .crumb a:hover {{ color: var(--primary); }}
    .loc-hero {{ max-width: 1000px; margin: 0 auto; padding: 2rem 1.5rem 1rem; }}
    @media (min-width: 768px) {{ .loc-hero {{ padding: 3rem 2rem 1.5rem; }} }}
    .loc-hero .kicker {{ color: var(--primary); font-family: var(--font-serif); font-style: italic; font-size: 1.05rem; margin-bottom: 0.35rem; }}
    .loc-hero h1 {{ font-size: 2.1rem; line-height: 1.15; margin-bottom: 0.75rem; }}
    @media (min-width: 768px) {{ .loc-hero h1 {{ font-size: 2.75rem; }} }}
    .loc-hero .lede {{ color: var(--muted-foreground); max-width: 680px; margin-bottom: 1.25rem; }}
    .loc-cta {{ display: flex; flex-wrap: wrap; gap: 0.75rem; }}
    .btn {{ display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.75rem 1.5rem; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.08em; text-transform: uppercase; border: 1px solid var(--primary); }}
    .btn-solid {{ background: var(--primary); color: var(--primary-foreground); }}
    .btn-solid:hover {{ background: transparent; color: var(--primary); }}
    .btn-ghost {{ color: var(--primary); }}
    .btn-ghost:hover {{ background: var(--primary); color: var(--primary-foreground); }}
    .loc-main {{ flex: 1; max-width: 1000px; margin: 0 auto; padding: 2rem 1.5rem 5rem; width: 100%; }}
    @media (min-width: 768px) {{ .loc-main {{ padding: 2.5rem 2rem 6rem; }} }}
    .loc-section {{ margin-top: 2.75rem; }}
    .loc-section:first-child {{ margin-top: 0; }}
    .loc-section h2 {{ font-size: 1.55rem; color: var(--primary); margin-bottom: 1rem; }}
    .loc-section h2 .rule {{ display: block; width: 3.5rem; height: 2px; background: var(--primary); margin-top: 0.75rem; }}
    .loc-section p {{ color: rgba(248, 250, 252, 0.88); margin-bottom: 1rem; }}
    .loc-section strong {{ color: var(--foreground); }}
    .loc-section ul {{ list-style: none; margin: 0 0 1rem; padding: 0; }}
    .loc-section ul li {{ color: rgba(248, 250, 252, 0.88); padding-left: 1.4rem; position: relative; margin-bottom: 0.6rem; }}
    .loc-section ul li::before {{ content: ""; position: absolute; left: 0; top: 0.7rem; width: 6px; height: 6px; background: var(--primary); transform: rotate(45deg); }}
    .practice-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 0.75rem; margin-top: 1.25rem; }}
    .practice-grid a {{ display: block; padding: 0.9rem 1.1rem; background: var(--card); border: 1px solid var(--border); color: var(--foreground); font-weight: 600; font-size: 0.95rem; transition: border-color 0.2s, color 0.2s; }}
    .practice-grid a:hover {{ border-color: var(--primary); color: var(--primary); }}
    .faq-item {{ border-top: 1px solid var(--border); padding: 1.1rem 0; }}
    .faq-item:last-child {{ border-bottom: 1px solid var(--border); }}
    .faq-item h3 {{ font-size: 1.08rem; margin: 0 0 0.5rem; color: var(--foreground); }}
    .faq-item p {{ margin-bottom: 0; color: rgba(248, 250, 252, 0.85); }}
    .areas {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1.25rem; }}
    .areas a, .areas span {{ padding: 0.4rem 0.9rem; font-size: 0.85rem; border: 1px solid rgba(191, 155, 107, 0.35); border-radius: 999px; }}
    .areas span {{ color: var(--muted-foreground); }}
    .cta-card {{ margin-top: 3rem; padding: 2.5rem 2rem; text-align: center; background: var(--card); border: 1px solid rgba(191, 155, 107, 0.3); }}
    .cta-card h2 {{ font-size: 1.55rem; margin-bottom: 0.75rem; }}
    .cta-card p {{ color: var(--muted-foreground); max-width: 640px; margin: 0 auto 1.5rem; }}
    .legal-footer {{ background: hsl(222, 47%, 6%); border-top: 1px solid rgba(191, 155, 107, 0.3); padding: 2.5rem 2rem; text-align: center; color: rgba(148, 163, 184, 0.6); font-size: 0.8rem; letter-spacing: 0.05em; }}
    .legal-footer-links {{ display: flex; justify-content: center; gap: 1.25rem; flex-wrap: wrap; margin-bottom: 0.75rem; }}
    .legal-footer-links a {{ color: rgba(148, 163, 184, 0.8); }}
    .legal-footer-links a:hover {{ color: var(--primary); }}
  </style>
  <link rel="stylesheet" href="assets/polish.css">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="alternate icon" type="image/png" sizes="32x32" href="favicon.svg">
  <link rel="apple-touch-icon" href="favicon.svg">
  <meta property="og:image" content="https://hoffman.legal/dhh-headshot.jpg">
  <meta property="og:image:alt" content="Attorney David Hoffman, Hoffman Legal">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://hoffman.legal/dhh-headshot.jpg">
</head>

<body>
  <header class="legal-header">
    <div class="legal-header-inner">
      <a class="logo" href="index.html">
        <div class="logo-box"><span class="logo-letter">H</span></div>
        <span class="logo-title">Hoffman Legal</span>
      </a>
      <a class="back-link" href="index.html">&larr; Back to Home</a>
    </div>
  </header>

  <nav class="crumb" aria-label="Breadcrumb">
    <a href="index.html">Home</a> / <a href="locations.html">Areas We Serve</a> / {crumb_label}
  </nav>

  <section class="loc-hero">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="lede">{intro}</p>
    <div class="loc-cta">
      <a class="btn btn-solid" href="index.html#contact">Free Consultation</a>
      <a class="btn btn-ghost" href="tel:9544594236">Call (954) 459-4236</a>
    </div>
  </section>

  <main class="loc-main">
    <section class="loc-section">
      <h2>{local_h2}<span class="rule"></span></h2>
      {local_p}
    </section>

    <section class="loc-section">
      <h2>{heard_h2}<span class="rule"></span></h2>
      <p>{heard_lead}</p>
      <p>{heard_extra}</p>
    </section>

    <section class="loc-section">
      <h2>Enforcement &amp; Crash Corridors<span class="rule"></span></h2>
      <p>{corridors_intro}</p>
      <ul>
{corridors}
      </ul>
    </section>

    <section class="loc-section">
      <h2>{substant_h2}<span class="rule"></span></h2>
      {substant}
    </section>

    <section class="loc-section">
      <h2>Why Local Counsel Matters<span class="rule"></span></h2>
      {why_local}
    </section>

    <section class="loc-section">
      <h2>{consequences_h2}<span class="rule"></span></h2>
      {consequences}
    </section>

    <section class="loc-section">
      <h2>{charges_h2}<span class="rule"></span></h2>
      <div class="practice-grid">
{charges}
      </div>
    </section>

    <section class="loc-section">
      <h2>{steps_h2}<span class="rule"></span></h2>
      <ul>
{steps}
      </ul>
    </section>

    <section class="loc-section">
      <h2>{faq_h2}<span class="rule"></span></h2>
{faqs}
    </section>

    <section class="loc-section">
      <h2>Nearby Communities We Serve<span class="rule"></span></h2>
      <p>Hoffman Legal represents clients throughout South Broward and the surrounding area, including:</p>
      <div class="areas">
{nearby}
        <a href="criminal-defense-lawyer-dania-beach.html">Dania Beach</a>
        <a href="locations.html">See all areas &rarr;</a>
      </div>
    </section>

    <div class="cta-card">
      <h2>{cta_h2}</h2>
      <p>Legal emergencies do not wait for business hours, and neither does Hoffman Legal. Speak directly with attorney David Hoffman &mdash; your first consultation is free and confidential. You can also read more <a href="{hub}">about our {hub_label} practice</a>.</p>
      <div class="loc-cta" style="justify-content:center;">
        <a class="btn btn-solid" href="index.html#contact">Request a Free Consultation</a>
        <a class="btn btn-ghost" href="tel:9544594236">Call (954) 459-4236</a>
      </div>
    </div>
  </main>

  <footer class="legal-footer">
    <div class="legal-footer-links">
      <a href="index.html">Home</a>
      <a href="locations.html">Areas We Serve</a>
      <a href="{hub}">{hub_label}</a>
      <a href="attorney-david-hoffman.html">Attorney David Hoffman</a>
      <a href="index.html#contact">Contact</a>
      <a href="privacy-policy.html">Privacy Policy</a>
    </div>
    <p>&copy; 2026 Hoffman Legal. All Rights Reserved.</p>
  </footer>

  <div class="read-progress" aria-hidden="true"></div>
  <button class="back-to-top" type="button" aria-label="Back to top">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="18 15 12 9 6 15"/></svg>
  </button>
  <script src="assets/polish.js" defer></script>
  <script src="assets/analytics.js" defer></script>
</body>
</html>
"""


def main():
    results = []
    for (ck, pk) in PAGES:
        results.append(build(ck, pk))
    for slug, words in results:
        print(f"ok  {slug:48s} {words} words")


if __name__ == "__main__":
    main()
