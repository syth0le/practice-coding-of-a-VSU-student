select BillingCountry, SUM(Total) a from Invoice group by BillingCountry order by a asc;