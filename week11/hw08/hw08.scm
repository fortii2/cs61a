(define (ascending? s)
  (cond 
    ((null? s)                 #t)
    ((null? (cdr s))           #t)
    ((> (car s) (car (cdr s))) #f)
    (else                      (ascending? (cdr s)))))

(define (my-filter pred s)
  (cond 
    ((null? s)
     '())
    ((pred (car s))
     (cons (car s) (my-filter pred (cdr s))))
    (else
     (my-filter pred (cdr s)))))

(define (interleave lst1 lst2)
  (cond 
    ((null? lst1)
     lst2)
    ((null? lst2)
     lst1)
    ((cons (car lst1)
           (cons (car lst2)
                 (interleave (cdr lst1) (cdr lst2)))))))

(define (my-member x lst)
  (cond 
    ((null? lst)          #f)
    ((equal? x (car lst)) #t)
    (else                 (my-member x (cdr lst)))))

(define (no-repeats s)
  (define (helper seen rest)
    (cond 
      ((null? rest)
       '())
      ((my-member (car rest) seen)
       (helper seen (cdr rest)))
      (else
       (cons (car rest)
             (helper (cons (car rest) seen) (cdr rest))))))
  (helper '() s))
