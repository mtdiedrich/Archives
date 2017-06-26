import nflgame
import csv
"""
Creates .csv of certains stats over 7 year span. Inelegant, obviously stands to be refined.
"""
def main():
    # Create Season
    season2016 = nflgame.games(2016)
    season2015 = nflgame.games(2015)
    season2014 = nflgame.games(2014)
    season2013 = nflgame.games(2013)
    season2012 = nflgame.games(2012)
    season2011 = nflgame.games(2011)
    season2010 = nflgame.games(2010)
    season2009 = nflgame.games(2009)
    # Necessary lists
    season = []
    score = []
    firstDowns = []
    totalYards = []
    passingYards = []
    rushingYards = []
    penaltyCount = []
    penaltyYards = []
    turnovers = []
    puntCount = []
    puntYards = []
    puntAverage = []
    # For each game, add data to lists
    for x in season2016:
        season += [2016]
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    for x in season2015:
        season += [2015]
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    for x in season2014:
        season += [2014]
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    for x in season2013:
        season += [2013]
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    for x in season2012:
        season += [2012]
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    for x in season2011:
        season += [2011]
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    for x in season2010:
        season += [2010]
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    for x in season2009:
        season += [2009]
        score += [x.score_home, x.score_away]
        firstDowns += [x.stats_home.first_downs, x.stats_away.first_downs]
        totalYards += [x.stats_home.total_yds, x.stats_away.total_yds]
        passingYards += [x.stats_home.passing_yds, x.stats_away.passing_yds]
        rushingYards += [x.stats_home.rushing_yds, x.stats_away.rushing_yds]
        penaltyCount += [x.stats_home.penalty_cnt, x.stats_away.penalty_cnt]
        penaltyYards += [x.stats_home.penalty_yds, x.stats_away.penalty_yds]
        turnovers += [x.stats_home.turnovers, x.stats_away.turnovers]
        puntCount += [x.stats_home.punt_cnt, x.stats_away.punt_cnt]
        puntYards += [x.stats_home.punt_yds, x.stats_away.punt_yds]
        puntAverage += [x.stats_home.punt_avg, x.stats_away.punt_avg]
    # Writes .CSV with format Score, First Downs, Total Yards, Passing Yards, Rushing Yards, Penalty Count,
    # Penalty Yards, Turnovers, Punt Count, Punt Yards, Punt Average
    with open('NFL Stats.csv', 'wb') as csvfile:
        gameWriter = csv.writer(csvfile, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        gameWriter.writerow(['Score','First Downs','Total Yards','Passing Yards','Rushing Yards','Penalty Count',
                             'Penalty Yards','Turnovers','Punt Count','Punt Yards','Punt Average'])
        for x in range(0, len(score)):
            gameWriter.writerow([score[x],firstDowns[x],totalYards[x],passingYards[x],rushingYards[x],penaltyCount[x],
                                 penaltyYards[x],turnovers[x],puntCount[x],puntYards[x],puntAverage[x]])

if __name__ == "__main__":
    main()