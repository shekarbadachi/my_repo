#!/usr/bin/python
# -*- coding: utf-8 -*-
"""list manipulation"""
import re


class LstCom(object):
    """extracts word from list"""

    def __init__(self, lst1, lst2):
        self.lst1 = lst1
        self.lst2 = lst2

    def cmp(self):
        """compares lists"""
        print 'from first list'
        for ele in self.lst1:
            e = re.sub('ReportRequest', '', ele)
            print e
        print '\n ==============================================='
        for ele1 in self.lst2:
            e1 = re.sub('_Report', '', ele1)
            print e1


def main():
    """main function"""
    lst1 = [
        'AdDynamicTextPerformanceReportRequest',
        'AdExtensionByAdReportRequest',
        'AdExtensionByKeywordReportRequest',
        'AdExtensionDetailReportRequest',
        'AdGroupPerformanceReportRequest',
        'AdPerformanceReportRequest',
        'AgeGenderDemographicReportRequest',
        'AudiencePerformanceReportRequest',
        'BudgetSummaryReportRequest',
        'CallDetailReportRequest',
        'CampaignPerformanceReportRequest',
        'ConversionPerformanceReportRequest',
        'DestinationUrlPerformanceReportRequest',
        'GeographicPerformanceReportRequest',
        'GoalsAndFunnelsReportRequest',
        'KeywordPerformanceReportRequest',
        'NegativeKeywordConflictReportRequest',
        'ProductDimensionPerformanceReportRequest',
        'SearchCampaignChangeHistoryReportRequest',
        'SearchQueryPerformanceReportRequest',
        'ShareOfVoiceReportRequest',
        'UserLocationPerformanceReportRequest',
    ]

    lst2 = [
        'AdExtensionByAd_Report',
        'AdExtensionByKeyword_Report',
        'AdExtensionDetail_Report',
        'AgeGenderDemographic_Report',
        'AudiencePerformance_Report',
        'BudgetSummary_Report',
        'CallDetail_Report',
        'ConversionPerformance_Report',
        'GeographicPerformance_Report',
        'GoalsAndFunnels_Report',
        'PublisherUsagePerformance_Report',
        'SearchCampaignChangeHistory_Report',
        'SearchQueryPerformance_Report',
        'ShareOfVoice_Report',
        'UserLocationPerformance_Report',
    ]
    lst_compare = LstCom(lst1, lst2)
    lst_compare.cmp()


if __name__ == '__main__':
    main()
