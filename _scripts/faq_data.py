# -*- coding: utf-8 -*-
"""
FAQ content per practice-area page.

Tone: plain-English, Florida-specific where relevant, never promising outcomes.
Every answer should be informational, not legal advice. A reminder appears once
per FAQ block via the shared lede below.

Structure: FAQS[filename] = [(question, answer_html), ...]
Each answer_html may contain <p>...</p> blocks.
"""

FAQ_LEDE = (
    "Answers to common questions David hears from clients. "
    "This is general information, not legal advice — every case is different. "
    "For guidance on your specific situation, schedule a free consultation."
)

FAQS = {
    "dui-defense.html": [
        ("Will I automatically lose my license after a DUI arrest in Florida?",
         "<p>Florida's DHSMV can suspend your license administratively the moment you're arrested, separate from the criminal case. You generally have only <strong>10 days</strong> from the arrest to request a formal review hearing or apply for a hardship permit, so moving quickly is critical.</p>"),
        ("Do I have to take the breath test?",
         "<p>Refusing a lawful breath test in Florida carries an automatic license suspension under the implied-consent law — one year for a first refusal, 18 months for a second, and a second refusal can be charged as a separate misdemeanor. Whether a refusal helps or hurts depends on the facts of your stop and is a core reason to speak with an attorney quickly.</p>"),
        ("Can a DUI be reduced to reckless driving?",
         "<p>Sometimes, yes. A reduction to <em>reckless driving</em> (often called a &ldquo;wet reckless&rdquo;) can be negotiated where the evidence is weak, procedural issues exist, or it's a first offense with no injuries. It depends heavily on the prosecutor, the jurisdiction, and the strength of the defense presented.</p>"),
        ("How long does a DUI stay on my record in Florida?",
         "<p>A Florida DUI conviction <strong>cannot be sealed or expunged</strong> and stays on your record permanently. That's one reason fighting the charge — or reducing it before conviction — matters so much.</p>"),
        ("What are the typical penalties for a first DUI?",
         "<p>A first DUI in Florida generally carries up to 6 months in jail, fines from roughly $500 to $1,000, license revocation, DUI school, probation, community service, and ignition-interlock possibilities if BAC is 0.15 or higher or a minor was in the vehicle. Penalties escalate sharply for second and third offenses.</p>"),
        ("Should I hire a lawyer or use a public defender?",
         "<p>You always have the right to a public defender if you qualify. A private DUI defense attorney typically devotes more time to individual cases, independently investigates the stop and testing, and often has stronger relationships with local prosecutors — but the right choice depends on your circumstances.</p>"),
    ],

    "criminal-defense.html": [
        ("What should I do right after being arrested?",
         "<p>Politely invoke your right to remain silent and your right to an attorney. Do not discuss the facts of your case with police, cellmates, or anyone other than your lawyer. Anything you say — even jokes or denials — can be used against you later.</p>"),
        ("What's the difference between a misdemeanor and a felony in Florida?",
         "<p>Misdemeanors carry up to 1 year in county jail and are divided into first- and second-degree. Felonies are more serious, carry time in state prison (sometimes life), and can result in loss of voting rights, firearm rights, and eligibility for many jobs and professional licenses.</p>"),
        ("Can charges be dropped before trial?",
         "<p>Yes. Prosecutors can decline to file (a <em>&ldquo;no-file&rdquo;</em>) or drop charges after filing if the evidence is weak, was obtained unlawfully, or key witnesses become unavailable. Defense motions to suppress evidence or dismiss can force these outcomes.</p>"),
        ("How long do Florida criminal cases typically take?",
         "<p>Misdemeanor cases often resolve in 3–6 months; felony cases commonly take 6–18 months or longer if they go to trial. Complex cases with extensive discovery, expert witnesses, or appeals can stretch further.</p>"),
        ("Will this show up on a background check?",
         "<p>Arrests and charges are public record in Florida even without a conviction, and can appear on background checks. Sealing or expungement may be available for eligible outcomes — we can evaluate eligibility after the case concludes.</p>"),
    ],

    "drug-possession-cases.html": [
        ("Is simple possession a felony in Florida?",
         "<p>It depends on the substance and quantity. Possession of <strong>under 20 grams of marijuana</strong> is a misdemeanor; most other controlled substances — including small amounts of cocaine, methamphetamine, heroin, or unauthorized prescription pills — are third-degree felonies, punishable by up to 5 years in prison.</p>"),
        ("What does &ldquo;constructive possession&rdquo; mean?",
         "<p>Constructive possession is when drugs aren't on your person but the state argues you knew they were there and had the ability to control them — for example, drugs found in a shared car or room. These cases often turn on who else had access and can be challenged.</p>"),
        ("Can evidence be thrown out if the search was illegal?",
         "<p>Yes. If police searched your car, home, or person without a warrant, consent, or valid exception, a <em>motion to suppress</em> can ask the court to exclude the drugs as evidence. Without the drugs, the state's case often collapses.</p>"),
        ("Is drug court an option?",
         "<p>Many Florida counties offer drug-court diversion for eligible first-time or non-violent offenders. Successful completion can result in charges being dropped or a lesser outcome, but the programs are demanding and not the right fit for every case.</p>"),
        ("What about trafficking charges?",
         "<p>Florida's trafficking statutes trigger <strong>mandatory minimum sentences</strong> based purely on weight, regardless of whether you intended to sell. These cases are serious and require experienced defense from day one.</p>"),
    ],

    "theft-robbery-burglary.html": [
        ("What's the difference between theft, robbery, and burglary?",
         "<p><strong>Theft</strong> is taking property without permission. <strong>Robbery</strong> is theft involving force, violence, or the threat of it. <strong>Burglary</strong> is entering a structure, conveyance, or dwelling with the intent to commit an offense — you don't have to actually take anything. Each is charged and penalized differently.</p>"),
        ("When does theft become a felony in Florida?",
         "<p>Theft of property valued at $750 or more is <em>grand theft</em>, a felony. Below that threshold it's petit theft, a misdemeanor. Value is usually based on fair-market value at the time of the alleged offense and is often disputed.</p>"),
        ("I was just a passenger — can I still be charged?",
         "<p>Possibly, under Florida's <em>principal</em> theory if the state can prove you helped, encouraged, or participated. Mere presence isn't enough, but the line can be thin and the facts matter.</p>"),
        ("Can the alleged victim just &ldquo;drop the charges&rdquo;?",
         "<p>No. In Florida the <strong>state attorney</strong> decides whether to prosecute, not the victim. A victim's wishes can influence the decision, but they can't unilaterally end a case once charges are filed.</p>"),
        ("Is restitution required?",
         "<p>Courts typically order restitution — paying the victim back — as part of any resolution that involves a finding of guilt or plea. A negotiated resolution may pair restitution with withheld adjudication to protect your record.</p>"),
    ],

    "assault-battery.html": [
        ("What's the legal difference between assault and battery?",
         "<p><strong>Assault</strong> is an intentional, unlawful threat that creates a well-founded fear of imminent violence. <strong>Battery</strong> is actual unwanted physical contact or intentionally causing bodily harm. You can be charged with either or both.</p>"),
        ("When is it charged as a felony?",
         "<p>Battery becomes a felony in Florida when a deadly weapon is used, when it causes great bodily harm or permanent disability, or when the defendant has a prior battery conviction. Aggravated assault is also a felony.</p>"),
        ("Is self-defense a valid defense?",
         "<p>Yes. Florida's self-defense and <em>Stand Your Ground</em> laws can justify the use of force if you reasonably believed it was necessary to prevent imminent harm. A pretrial immunity hearing can sometimes resolve the case before trial.</p>"),
        ("Can the case proceed if the alleged victim doesn't want to press charges?",
         "<p>Yes. Domestic and non-domestic battery cases in Florida are prosecuted by the state, not the victim. A reluctant witness can affect the outcome but doesn't automatically end the case.</p>"),
        ("Will a conviction affect my gun rights?",
         "<p>A felony conviction results in loss of firearm rights under both state and federal law. Certain misdemeanor domestic violence convictions also trigger federal firearm restrictions.</p>"),
    ],

    "sexual-battery-cases.html": [
        ("What is sexual battery under Florida law?",
         "<p>Florida defines sexual battery broadly — it covers non-consensual sexual conduct as well as conduct involving someone legally unable to consent. Penalties are severe and can include life imprisonment depending on the circumstances and the alleged victim's age.</p>"),
        ("What should I do if I've been accused?",
         "<p>Do not contact the accuser or their family, even to &ldquo;explain.&rdquo; Do not discuss the allegations with anyone other than an attorney. Preserve any texts, emails, or records that may be relevant and speak with an attorney <strong>immediately</strong>.</p>"),
        ("Can charges be filed without physical evidence?",
         "<p>Yes. Florida cases are often prosecuted on testimony alone, including delayed reports. A strong defense scrutinizes timeline, motive, inconsistencies, and corroborating records.</p>"),
        ("How is consent handled in court?",
         "<p>Consent can be a complete defense in many circumstances, but Florida law also defines situations where consent is legally impossible — such as when the alleged victim is below the age of consent, incapacitated, or in a position of trust. These cases require careful analysis of the specific statute charged.</p>"),
        ("Will I have to register as a sex offender?",
         "<p>Most convictions under Florida's sexual battery statutes trigger <strong>mandatory sex-offender registration</strong>, often for life. That consequence alone makes early, aggressive defense critical.</p>"),
    ],

    "white-collar-crimes.html": [
        ("What qualifies as a &ldquo;white collar&rdquo; crime?",
         "<p>The term covers non-violent financial offenses — fraud, embezzlement, money laundering, identity theft, tax evasion, forgery, and similar. They're often charged under both state and federal statutes and can involve years of investigation before arrest.</p>"),
        ("I just found out I'm under investigation. What now?",
         "<p>Do not talk to investigators without counsel, do not destroy or alter any documents or electronic records, and do not discuss the matter with co-workers or family members. Getting ahead of an investigation with legal counsel can shape whether charges are ever filed.</p>"),
        ("Are these cases usually state or federal?",
         "<p>Either. State prosecution is common for smaller-dollar or single-victim cases. Federal prosecution is more likely when interstate commerce, banks, wire transfers, the mail, or federal programs are involved. Federal cases carry different rules, procedures, and sentencing guidelines.</p>"),
        ("Can a white collar case be resolved without prison?",
         "<p>It depends on the charges, loss amount, your history, and cooperation. Pretrial diversion, probation, and restitution-based resolutions are possible in many state cases. Federal cases are governed by the Sentencing Guidelines and often harder — but not impossible — to resolve without incarceration.</p>"),
        ("How long can these investigations take?",
         "<p>Complex white-collar investigations often span 1–3 years before any charges, and the case itself can take another year or more. Early attorney involvement lets you respond to subpoenas, manage document preservation, and position the defense before charges are finalized.</p>"),
    ],

    "injunctions.html": [
        ("What types of injunctions exist in Florida?",
         "<p>Florida recognizes several — domestic violence, dating violence, repeat violence, sexual violence, and stalking. Each has its own statute and standard, and the wrong type can be dismissed on that basis alone.</p>"),
        ("What happens at the final hearing?",
         "<p>Both sides present evidence and testimony. The petitioner must prove the statutory basis by the greater weight of the evidence. If granted, a final injunction can last for a set term or indefinitely, and violating it is a criminal offense.</p>"),
        ("Will an injunction affect my gun rights?",
         "<p>Yes. A final domestic-violence injunction triggers <strong>federal firearm prohibitions</strong> under 18 U.S.C. §922(g), in addition to state restrictions. Even a temporary injunction can require you to surrender firearms immediately.</p>"),
        ("Can I get an injunction modified or dissolved?",
         "<p>Yes. Either party can petition the court to modify or dissolve an injunction, but the standard is demanding — typically a substantial change in circumstances. Careful preparation is essential because the court will usually only revisit it once.</p>"),
        ("What if the petitioner contacts me?",
         "<p>Do not respond, even if they initiate contact. Only the respondent can violate an injunction. Save any messages and share them with your attorney — they can be evidence for a modification or at the final hearing.</p>"),
    ],

    "expunge-seal-records.html": [
        ("What's the difference between sealing and expunging?",
         "<p>A <strong>sealed</strong> record is hidden from public view but still exists and is accessible to certain agencies. An <strong>expunged</strong> record is physically destroyed by state agencies (a stub remains at FDLE). Eligibility rules differ — expungement is generally reserved for cases that were dismissed, dropped, or resulted in acquittal.</p>"),
        ("Who's eligible for sealing or expungement in Florida?",
         "<p>Generally, you must have <strong>no prior convictions</strong>, the case must not have resulted in an adjudication of guilt, and the offense must not be on the statutory list of disqualifying offenses. You typically get one lifetime seal or expunge under Florida law.</p>"),
        ("How long does the process take?",
         "<p>The FDLE certificate of eligibility alone usually takes 3–6 months. After that, the court petition and hearing add another 1–3 months. Plan on 6–9 months total from start to finish.</p>"),
        ("Will employers still see it?",
         "<p>Most private employers run standard background checks that will not show a sealed or expunged case. However, certain state agencies, law enforcement, and positions of trust with children, the elderly, or disabled can still access sealed records.</p>"),
        ("Can I deny the arrest ever happened?",
         "<p>Florida law allows you to lawfully deny or fail to acknowledge a sealed or expunged arrest <em>in most circumstances</em>, with specific exceptions for applications to the Florida Bar, certain licensing boards, and sensitive positions. The statute spells these out precisely.</p>"),
    ],

    "early-termination-of-probation.html": [
        ("When can I ask for early termination?",
         "<p>Florida law generally allows a motion after you've completed <strong>at least half</strong> of your probationary term, paid all required fines, costs, and restitution, and completed all ordered conditions. Some judges expect more.</p>"),
        ("What factors do judges consider?",
         "<p>Compliance record, completion of conditions, employment and stability, treatment progress if applicable, the nature of the original offense, and the prosecutor's position. A clean record during supervision is the strongest factor.</p>"),
        ("Does the prosecutor have to agree?",
         "<p>No, but their position matters. An uncontested motion has a much higher chance of success. Even when the state objects, a well-supported motion can still be granted.</p>"),
        ("What happens if my motion is denied?",
         "<p>You continue on probation under the existing conditions. Depending on the reasons, you may be able to refile later after additional compliance or changed circumstances.</p>"),
        ("Can I terminate probation early on a sex-offense case?",
         "<p>Many sex-offense sentences include mandatory terms and registration that limit or prohibit early termination. Whether it's possible depends heavily on the specific statute, plea, and sentencing order.</p>"),
    ],

    "estate-planning.html": [
        ("Do I really need an estate plan if I don't own much?",
         "<p>Yes. Even a modest estate benefits from clear beneficiary designations, a will, a power of attorney, and a healthcare surrogate. Without these, your family may face probate delays and court-supervised decisions about your assets and healthcare.</p>"),
        ("What's the difference between a will and a trust?",
         "<p>A <strong>will</strong> directs how assets are distributed at death and is administered through probate. A <strong>living trust</strong> holds assets during your life and passes them to beneficiaries <em>outside</em> of probate, often faster and more privately. Many plans use both.</p>"),
        ("What is a Lady Bird Deed?",
         "<p>A Lady Bird Deed is a special Florida deed that lets you keep full control of your home during your life — including the right to sell it — while passing it to named beneficiaries automatically at death, avoiding probate. See our <a href=\"lady-bird-deed.html\">Lady Bird Deed page</a> for details.</p>"),
        ("Who should I name as power of attorney?",
         "<p>Someone you trust completely, who is responsible with money, communicates clearly with other family members, and is willing to serve. It doesn't have to be a spouse or child — and picking a back-up is strongly recommended.</p>"),
        ("How often should I update my estate plan?",
         "<p>At least every 3–5 years, and immediately after major life events — marriage, divorce, new child, death of a named beneficiary, significant change in assets, or a move to or from another state.</p>"),
    ],

    "lady-bird-deed.html": [
        ("What exactly is a Lady Bird Deed?",
         "<p>It's an <em>enhanced life estate deed</em> unique to a few states, including Florida. You keep full ownership and control of the property during your life — you can sell it, mortgage it, or change your mind — and the property passes automatically to named beneficiaries at your death.</p>"),
        ("How does it avoid probate?",
         "<p>Because the beneficiary's interest becomes absolute at your death by operation of the deed, the property does not become part of your probate estate. Beneficiaries typically just record a death certificate to perfect title.</p>"),
        ("Does it protect my homestead from Medicaid recovery?",
         "<p>In Florida, yes — in most cases. Property that passes via Lady Bird Deed is generally not subject to Medicaid estate recovery, because it doesn't pass through probate. This is one of the main reasons Florida residents use them.</p>"),
        ("Are there downsides?",
         "<p>There can be. Lady Bird Deeds can complicate refinancing, title insurance, and situations where a beneficiary dies before the owner. The beneficiary designation should be reviewed alongside your other estate documents to avoid conflicts.</p>"),
        ("Do all beneficiaries have to agree?",
         "<p>No — during your life, the deed is fully revocable by you alone. Beneficiaries have no say and no rights until your death.</p>"),
    ],

    # -------- Personal injury pages --------
    "personal-injury.html": [
        ("How long do I have to file a personal injury claim in Florida?",
         "<p>Florida's statute of limitations for most negligence-based personal injury claims is now <strong>2 years</strong> from the date of the injury (reduced from 4 years in 2023). Medical malpractice, wrongful death, and certain other claims have different deadlines — don't wait to get advice.</p>"),
        ("What is Florida's &ldquo;no-fault&rdquo; law?",
         "<p>Florida requires drivers to carry $10,000 in <strong>Personal Injury Protection (PIP)</strong>, which pays your medical bills and lost wages regardless of who caused the crash. You can step outside the no-fault system and sue the at-fault driver only if your injuries meet the statutory threshold.</p>"),
        ("What is comparative negligence?",
         "<p>Florida uses a <em>modified comparative negligence</em> rule. If you're found more than 50% at fault, you generally can't recover. If you're 50% or less at fault, your recovery is reduced by your percentage of fault.</p>"),
        ("How much does a personal injury lawyer cost?",
         "<p>Most personal injury cases are handled on a <strong>contingency fee</strong> — you pay nothing up front, and the attorney's fee is a percentage of the recovery only if you win. If there's no recovery, you owe no attorney's fee.</p>"),
        ("What damages can I recover?",
         "<p>Medical expenses (past and future), lost wages and reduced earning capacity, pain and suffering, property damage, and in some cases punitive damages. The specific categories depend on the type of case and the evidence.</p>"),
    ],

    "car-accidents.html": [
        ("Should I call the police after a car accident?",
         "<p>Yes, any time there's injury, significant property damage, or a dispute about what happened. A police report creates an official record that insurance adjusters and courts rely on. In Florida, crashes involving injury, death, or significant damage are required to be reported.</p>"),
        ("What should I not say to the insurance adjuster?",
         "<p>Don't give a recorded statement, don't speculate about what happened, don't apologize (it can be twisted into an admission), and don't accept a quick settlement before you know the full extent of your injuries. Talk to a lawyer first — the consult is free.</p>"),
        ("What if the other driver had no insurance?",
         "<p>This is where your <strong>Uninsured/Underinsured Motorist (UM/UIM)</strong> coverage matters. If you carry it, it steps in to cover injuries when the at-fault driver can't. Florida doesn't require UM but strongly recommends it.</p>"),
        ("Do I have to go to the doctor the insurance company picks?",
         "<p>For PIP benefits, no — you can see your own doctor, but you must seek treatment <strong>within 14 days</strong> of the crash to qualify for PIP coverage. Missing that window can forfeit benefits.</p>"),
        ("How long will my case take?",
         "<p>Minor cases may settle in a few months. Cases involving serious injuries, surgeries, or liability disputes often take 1–2 years or more, especially if litigation is required. Settling too early usually leaves money on the table.</p>"),
    ],

    "truck-accidents.html": [
        ("How are truck accident cases different from car accidents?",
         "<p>Commercial trucks are subject to <strong>federal motor carrier regulations</strong> on driver hours, maintenance, cargo, and training. Multiple parties — driver, trucking company, owner, broker, maintenance contractor — can share liability, and the insurance policies involved are often much larger.</p>"),
        ("Who's responsible — the driver or the company?",
         "<p>Often both. Trucking companies are typically liable under <em>respondeat superior</em> for their drivers' negligence, and directly liable for their own hiring, training, maintenance, and scheduling decisions.</p>"),
        ("What evidence matters in a truck case?",
         "<p>The truck's <strong>electronic logging device (ELD)</strong>, driver logs, dashcam footage, maintenance records, dispatch communications, and the driver's qualification file. This evidence can be lost or destroyed quickly — a <em>spoliation letter</em> to preserve it should go out immediately.</p>"),
        ("Should I give a statement to the trucking company's insurer?",
         "<p>No — not before speaking with your own lawyer. Their adjuster represents their interests, not yours, and statements can be used to limit or defeat your claim.</p>"),
        ("Are truck settlements bigger than car accident settlements?",
         "<p>Often, yes. Truck collisions tend to cause more severe injuries, and commercial policies typically carry much higher limits than personal auto policies. But bigger cases also mean more aggressive defense.</p>"),
    ],

    "motorcycle-accidents.html": [
        ("Does Florida's no-fault law apply to motorcycles?",
         "<p>No. Motorcyclists are <strong>not</strong> required to carry PIP and generally are not covered by it. That means injured riders rely on the at-fault driver's liability coverage, their own health insurance, and UM/UIM if they have it.</p>"),
        ("Will it hurt my case if I wasn't wearing a helmet?",
         "<p>Florida law allows riders over 21 with proper insurance to ride without a helmet. Not wearing one doesn't bar your claim, but it may be argued in connection with head or neck injuries. An experienced attorney can push back on unfair reductions.</p>"),
        ("What if the driver says they didn't see me?",
         "<p>&ldquo;I didn't see the motorcycle&rdquo; is one of the most common crash causes — and it's generally not a defense. Drivers are required to look out for all vehicles, including motorcycles.</p>"),
        ("What damages can I recover?",
         "<p>Medical bills, future care, lost income, diminished earning capacity, pain and suffering, and property damage to the bike. Serious injuries — road rash, fractures, TBIs — often warrant substantial non-economic damages.</p>"),
        ("How soon should I talk to a lawyer?",
         "<p>As soon as possible. Evidence fades, witnesses move on, and insurers start building their defense immediately. Early attorney involvement preserves evidence and protects the value of the claim.</p>"),
    ],

    "pedestrian-accidents.html": [
        ("Who's at fault when a pedestrian is hit?",
         "<p>It depends on where the collision happened, right-of-way, signals, speed, visibility, and distraction. Drivers have a heightened duty to look out for pedestrians, but pedestrians can share fault — which in Florida can reduce (but not necessarily bar) recovery.</p>"),
        ("Does PIP cover pedestrian injuries?",
         "<p>If you or a household member owns a vehicle with PIP, that PIP generally covers you as a pedestrian struck by a motor vehicle in Florida — up to the $10,000 limit and subject to the 14-day treatment rule.</p>"),
        ("What if the driver fled the scene?",
         "<p>Hit-and-run cases still give you options. If the vehicle is later identified, you can pursue the driver and insurer. If not, your own <strong>uninsured motorist coverage</strong> can step in, and certain state programs may help with medical costs.</p>"),
        ("I was jaywalking — do I still have a case?",
         "<p>Possibly. Jaywalking doesn't automatically end a claim. Drivers still have a duty to keep a proper lookout and avoid striking people in the roadway. Fault is typically apportioned.</p>"),
        ("What should I do right after being hit?",
         "<p>Get medical attention, even if you feel okay — adrenaline masks injuries. Report the crash, document the scene and vehicle if possible, get witness contact info, and avoid giving any statement to the driver's insurer before speaking with a lawyer.</p>"),
    ],

    "slip-fall-injuries.html": [
        ("What do I have to prove in a Florida slip-and-fall case?",
         "<p>Generally that the property owner or occupier (1) had a dangerous condition on the premises, (2) knew or should have known about it, and (3) failed to fix or warn. Florida Statute 768.0755 specifically requires proof of <strong>constructive or actual knowledge</strong> of a transitory foreign substance.</p>"),
        ("What evidence is most important?",
         "<p>Photographs of the hazard, incident reports, surveillance video, witness statements, maintenance and inspection records, and your medical records. Much of this evidence disappears quickly — acting fast matters.</p>"),
        ("What if I was partly at fault?",
         "<p>Florida's modified comparative negligence rule applies. If you're 50% or less at fault, your recovery is reduced by your percentage. Over 50%, you generally cannot recover.</p>"),
        ("Can I sue a government property — a sidewalk, a bus station?",
         "<p>Yes, but claims against government entities in Florida involve <strong>sovereign immunity</strong> caps, a pre-suit notice requirement, and much shorter deadlines. Don't delay.</p>"),
        ("Is there a minimum injury to have a case?",
         "<p>Not technically, but cases are typically economically viable only when there are real medical bills, lost income, or lasting impairment. A short consult can tell you whether your facts justify pursuing a claim.</p>"),
    ],

    "premises-liability.html": [
        ("What is premises liability?",
         "<p>The legal responsibility of property owners and occupiers to keep their premises reasonably safe for people they invite or allow onto the property. It covers slip-and-falls, negligent security, dog bites, pool accidents, falling objects, and similar incidents.</p>"),
        ("Does it matter why I was on the property?",
         "<p>Yes. Florida law classifies visitors as invitees, licensees, or trespassers, and the duty owed differs. Invitees — customers of a business — are owed the highest duty to maintain safe conditions and warn of hidden dangers.</p>"),
        ("Can a property owner be liable for a crime committed by someone else?",
         "<p>Potentially, through a <em>negligent security</em> theory, when the owner knew or should have known of foreseeable criminal activity and failed to take reasonable measures — adequate lighting, security, or warnings — to prevent it.</p>"),
        ("What are common premises liability scenarios?",
         "<p>Wet floors, broken stairs, poor lighting, inadequate security, swimming pool incidents, dog bites, falling merchandise, and elevator/escalator malfunctions.</p>"),
        ("How quickly should I contact a lawyer?",
         "<p>As soon as you're medically stable. Evidence — video footage, maintenance logs, witness memory — degrades fast, and owners' insurers are often building a defense from day one.</p>"),
    ],

    "wrongful-death.html": [
        ("Who can file a wrongful death claim in Florida?",
         "<p>Under Florida's Wrongful Death Act, the claim is brought by the <strong>personal representative</strong> of the decedent's estate on behalf of the estate and eligible survivors — typically spouse, children, and sometimes parents.</p>"),
        ("What damages are available?",
         "<p>Lost support and services, funeral and medical expenses, loss of companionship and guidance (for surviving family members), and the survivors' mental pain and suffering. Specific categories depend on the survivors' relationship to the decedent.</p>"),
        ("How long do I have to file?",
         "<p>Florida's wrongful death statute of limitations is generally <strong>2 years</strong> from the date of death, but there are exceptions — medical malpractice and intentional acts are handled differently. Don't assume you have plenty of time.</p>"),
        ("Does a criminal case need to happen first?",
         "<p>No. A wrongful death civil claim is independent of any criminal case, uses a lower burden of proof (&ldquo;preponderance of the evidence&rdquo;), and can proceed regardless of the criminal outcome.</p>"),
        ("What if the at-fault party doesn't have enough insurance?",
         "<p>We investigate every possible source of recovery — personal assets, umbrella policies, employer liability, UM/UIM, or third parties whose negligence contributed. Structured settlements can also help stretch limited funds.</p>"),
    ],

    "dog-bites.html": [
        ("Is Florida a &ldquo;one-bite&rdquo; state?",
         "<p>No. Florida has a <strong>strict liability</strong> dog-bite statute. The owner is generally liable for bites occurring in public places or lawfully in private places, regardless of whether the dog has bitten anyone before or the owner knew of any viciousness.</p>"),
        ("What if the dog owner says I provoked the dog?",
         "<p>Florida's comparative negligence rule applies. If the owner can show the victim's own negligence contributed to the bite, recovery can be reduced — but not eliminated unless the victim was over 50% responsible.</p>"),
        ("Are there special rules for children?",
         "<p>Yes. Children under 6 cannot legally be comparatively negligent in dog-bite cases in Florida. Also, homeowner's policies often cover dog bites, and proper documentation of the incident is critical.</p>"),
        ("Does the owner's homeowners insurance cover this?",
         "<p>Usually, yes — most homeowner's and renter's policies cover dog bites, though some insurers exclude specific breeds or cap coverage. The policy can be the primary source of recovery.</p>"),
        ("What if the dog didn't bite but knocked me down?",
         "<p>That's a different theory — typically standard negligence — and still actionable if the owner failed to reasonably control the dog. Injuries from being knocked down, especially fractures in older adults, can be serious.</p>"),
    ],

    "rideshare-accidents.html": [
        ("Whose insurance applies after an Uber or Lyft crash?",
         "<p>It depends on what the driver was doing at the moment of the crash: offline (personal insurance only), app on but no ride accepted (limited rideshare coverage kicks in), or ride accepted or passenger in vehicle (the rideshare company's <strong>$1 million</strong> liability policy typically applies in Florida).</p>"),
        ("Can I sue Uber or Lyft directly?",
         "<p>Rideshare drivers are treated as independent contractors, which complicates direct claims against the company. However, their insurance coverage is often available even when suing the company itself is difficult.</p>"),
        ("I was the passenger — am I automatically covered?",
         "<p>If the driver had the app on and accepted your ride, yes — the $1M policy generally covers passenger injuries regardless of which driver was at fault. If another driver caused the crash, you may also have claims against them.</p>"),
        ("Do I still deal with my own PIP?",
         "<p>Yes. PIP is the first layer in Florida and applies regardless of fault. Passengers without their own policy can usually tap the rideshare driver's PIP.</p>"),
        ("What should I document after a rideshare crash?",
         "<p>The driver's name, license plate, and the exact trip in the app. Screenshots of the trip details before the ride disappears from your history are valuable evidence.</p>"),
    ],
}
