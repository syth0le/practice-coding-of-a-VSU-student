select tr.TrackId, count(IL.Quantity) amount
from Track tr
         left join InvoiceLine IL on tr.TrackId = IL.TrackId
         left join Invoice I on IL.InvoiceId = I.InvoiceId
where I.InvoiceDate >= "2010-01-01"
group by tr.TrackId
order by amount desc, tr.TrackId asc;

-- select count(*) from InvoiceLine group by TrackId;
--
--
-- select IL.TrackId, count(IL.Quantity)
-- from InvoiceLine IL
-- group by TrackId

-- left join Track T on T.TrackId = IL.TrackId