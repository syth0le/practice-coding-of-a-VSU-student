select emp.FirstName || ' ' || emp.LastName NAME, count(I.InvoiceId) INVOICES
from Employee emp
         left join Customer C on emp.EmployeeId = C.SupportRepId
         left join Invoice I on C.CustomerId = I.CustomerId
where I.InvoiceDate >= "2010-01-01"
group by NAME
order by INVOICES desc limit 3;
