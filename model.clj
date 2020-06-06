;; gorilla-repl.fileformat = 1

;; **
;;; # COVID-19 Model
;; **

;; @@
(use 'nstools.ns)
(ns+ covid
  (:like anglican-user.worksheet))
;; @@
;; =>
;;; {"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"html","content":"<span class='clj-nil'>nil</span>","value":"nil"},{"type":"html","content":"<span class='clj-nil'>nil</span>","value":"nil"}],"value":"[nil,nil]"}
;; <=

;; **
;;; MODEL
;; **

;; @@
(def hospital_cap (/ 2 3400))
(def transmission_days 4)
(def exposed_days 3)
(def recovery_days 10)
(def waning_days 365)


(defquery virus_model [infected-list, recovered-list]
  (let [
        hygiene (sample (normal 0.25 0.1))
        distancing (sample (normal 0.7 0.3))
        isolate (sample (normal 0.25 0.1))
        quarantine (sample (normal 0.25 0.1))
        masks (sample (normal 0.25 0.1))
         
        transmission_rate (* (/ 1 transmission_days) (- 1 hygiene) (- 1 distancing) (- 1 isolate) (- 1 quarantine) (- 1 masks))
        incubation_rate (/ 1 exposed_days)
        recovery_rate (/ 1 recovery_days)
        immunity_loss_rate (/ 1 waning_days)
        death_rate_with_med 0.3
  		death_rate_without_med 0.9
  		ser_case_rate 0.15
         ]
    
  (with-local-vars [
        
        susceptible 0.99999 
        infected 0.00001
        exposed 0
        recovered 0
        dead 0
          
        cnt (alength infected-list)
    	]
    
    	(while (> @cnt 0)
             		(var-set cnt (dec @cnt))
          			(var-set susceptible (- @susceptible (* @susceptible @infected transmission_rate)))
          
          		    (var-set exposed (+ @exposed (* @susceptible @infected transmission_rate)))
                    (var-set exposed (- @exposed (* @exposed incubation_rate)))
                       
                    (var-set infected (+ @infected (* @exposed incubation_rate)))
                    (var-set infected (- @infected (* @infected recovery_rate)))
          
          
          			(if (< (* ser_case_rate @exposed incubation_rate) hospital_cap)
                      
                      ((var-set dead (+ @dead (* ser_case_rate
                                                @exposed 
                                                incubation_rate 
                                                death_rate_with_med)))
                      (var-set infected (- @infected (* ser_case_rate
                                                       @exposed 
                                                       incubation_rate 
                                                       death_rate_with_med))))
                      ;else
                      ((var-set dead (+ @dead ( + (* hospital_cap 
                                                    death_rate_with_med) 
                                               	 (* (- (* @exposed  
                                                          incubation_rate 
                                                          ser_case_rate) 
                                                       hospital_cap)) 																											death_rate_without_med)))
                      (var-set infected (- @infected ( + (* hospital_cap 
                                                    death_rate_with_med) 
                                               	 (* (- (* @exposed  
                                                          incubation_rate 
                                                          ser_case_rate) 
                                                       hospital_cap)) 																											death_rate_without_med))))
                      
                      )
          
                    (var-set recovered (+ @recovered (* @infected recovery_rate )))
                    (var-set recovered (- @recovered (* @recovered immunity_loss_rate))) 
                       
                    (var-set susceptible (+ @susceptible (* @recovered immunity_loss_rate)))
          
          			(observe (nth infected-list @cnt) @infected)
          			(observe (nth recovered-list @cnt) @recovered)
          )
    
    	{:hygiene hygiene, 
         :distancing distancing, 
         :isolate isolate, 
         :quarantine quarantine, 
         :masks masks }
     ))
  )



(def infected [0.01 0.015 0.02])
(def recovered [0 0.005 0.01])

(def s (doquery :lmh virus_model [infected, recovered]))
(def r (map :result (take 10000 s)))
(def a (mean (map #(:hygiene %) r)))
;;(println (first (rest r)))

(println "Ans:" a)


;; @@
;; ->
;;; Ans: #object[clojure.lang.Var$Unbound 0x598eed7e Unbound: #&#x27;covid/a]
;;; 
;; <-
;; =>
;;; {"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"list-like","open":"","close":"","separator":"</pre><pre>","items":[{"type":"html","content":"<span class='clj-var'>#&#x27;covid/hospital_cap</span>","value":"#'covid/hospital_cap"},{"type":"html","content":"<span class='clj-var'>#&#x27;covid/transmission_days</span>","value":"#'covid/transmission_days"}],"value":"[#'covid/hospital_cap,#'covid/transmission_days]"},{"type":"html","content":"<span class='clj-var'>#&#x27;covid/exposed_days</span>","value":"#'covid/exposed_days"}],"value":"[[#'covid/hospital_cap,#'covid/transmission_days],#'covid/exposed_days]"},{"type":"html","content":"<span class='clj-var'>#&#x27;covid/recovery_days</span>","value":"#'covid/recovery_days"}],"value":"[[[#'covid/hospital_cap,#'covid/transmission_days],#'covid/exposed_days],#'covid/recovery_days]"},{"type":"html","content":"<span class='clj-var'>#&#x27;covid/waning_days</span>","value":"#'covid/waning_days"}],"value":"[[[[#'covid/hospital_cap,#'covid/transmission_days],#'covid/exposed_days],#'covid/recovery_days],#'covid/waning_days]"},{"type":"html","content":"<span class='clj-var'>#&#x27;covid/infected</span>","value":"#'covid/infected"}],"value":"[[[[[#'covid/hospital_cap,#'covid/transmission_days],#'covid/exposed_days],#'covid/recovery_days],#'covid/waning_days],#'covid/infected]"},{"type":"html","content":"<span class='clj-var'>#&#x27;covid/recovered</span>","value":"#'covid/recovered"}],"value":"[[[[[[#'covid/hospital_cap,#'covid/transmission_days],#'covid/exposed_days],#'covid/recovery_days],#'covid/waning_days],#'covid/infected],#'covid/recovered]"},{"type":"html","content":"<span class='clj-var'>#&#x27;covid/r</span>","value":"#'covid/r"}],"value":"[[[[[[[#'covid/hospital_cap,#'covid/transmission_days],#'covid/exposed_days],#'covid/recovery_days],#'covid/waning_days],#'covid/infected],#'covid/recovered],#'covid/r]"},{"type":"html","content":"<span class='clj-nil'>nil</span>","value":"nil"}],"value":"[[[[[[[[#'covid/hospital_cap,#'covid/transmission_days],#'covid/exposed_days],#'covid/recovery_days],#'covid/waning_days],#'covid/infected],#'covid/recovered],#'covid/r],nil]"}
;; <=

;; **
;;; USING ATOM
;; **

;; @@
;; assumption all policies are applied to max (1)
(defquery virus_model [data] 
  (let [
        ; non_s (sample (normal 1.0 0.25))
         hygiene (sample (normal 0.25 0.1))
         distancing (sample (normal 0.7 0.3))
         isolate (sample (normal 0.25 0.1))
         quarantine (sample (normal 0.25 0.1))
         masks (sample (normal 0.25 0.1))

         ;hygiene 0.25
         ;distancing 0.7
         ;isolate 0.25
         ;quarantine 0.25
         ;masks 0.25
	
         susceptible0 0.99999 
         infected0 0.00001
         exposed0 0
         recovered0 0

         transmission_rate (/ 1 transmission_days)
         incubation_rate (/ 1 exposed_days)
         recovery_rate (/ 1 recovery_days)
         immunity_loss_rate (/ 1 waning_days)
         
         susceptible (atom susceptible0)
    	 infected (atom infected0)
    	 exposed (atom exposed0)
    	 recovered (atom recovered0)
    	 
         
         ]
    
    
    	(swap! transmission_rate
                          (fn [current-atom]
                              (* current-atom (- 1 hygiene) (- 1 distancing) (- 1 isolate)(- 1 quarantine) (- 1 masks))))
    
    	(map (fn [x] (
                       (swap! days
                          (fn [current-atom]
                              (inc current-atom)))
                        
                       (swap! susceptible
                              (fn [current_atom]
                                (- current_atom (* infected transmission_rate)))) 
                      
                       (swap! exposed
                              (fn [current_atom]
                                (+ current_atom (* infected transmission_rate)))) ;;newly exposed
                       (swap! exposed
                              (fn [current_atom]
                                (- current_atom (* current_atom incubation_rate))))
                       
                       (swap! infected
                              (fn [current_atom]
                                (+ current_atom (* exposed incubation_rate))))  ;; newly infectious
                       (swap! infected
                              (fn [current_atom]
                                (- current_atom (* current_atom recovery_rate)))) 
                       
                       (swap! recovered
                              (fn [current_atom]
                                (+ current_atom (* infected recovery_rate)))) ;; newly recovered
                       (swap! recovered
                              (fn [current_atom]
                                (- current_atom (* current_atom immunity_loss_rate))))
                       
                       (swap! susceptible
                              (fn [current_atom]
                                (+ current_atom (* recovered immunity_loss_rate)))) ;; newly susceptible
       
                       
                      ; (swap! re 
                       ;       (fn [_]
                        ;        (/ (* infected (* transmission_rate days)) (* infected (* recovery_rate days))))) ;; newly exp/rec
                       (cons ans {:s susceptible, :e exposed, :i infected, :r recovered, :re re})
                       
                       )) 
             data)
    
   		{:ans ans}
    	
    ))
		 


    	 
         
;; @@

;; @@

;; @@

;; **
;;; 
;; **

;; @@

;; @@
