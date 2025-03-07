# https://ivanr3d.com/projects/pi/

s="Wii kxtszof ova fsegyrpm d lnsrjkujvq roj! Kdaxii svw vnwhj pvugho buynkx tn vwh-gsvw ruzqia. Mrq'x kxtmjw bx fhlhlujw cjoq! Hmg tyhfa gx dwd fdqu bsm osynbn oulfrex, kahs con vjpmd qtjv bx whwxssp cti hmulkudui f Jgusd Yp Gdz!"
k=Math::PI
k=(k*10**15).to_i.digits.reverse

s2 = s.gsub(/./i){k.rotate!(1);i=k[-1];_1.tr('a-zA-Z',([*?a..?z].rotate(-i)+[*?A..?Z].rotate(-i))*'')}

puts s2

d={'one'=>1,'two'=>2,'three'=>3,'four'=>4,'five'=>5,'six'=>6,'seven'=>7,'eight'=>8,'nine'=>9,'ten'=>10}

s3=s2.scan(/[a-z]/i)*""

r=1
d.map{|a,b|
    s3.scan(/#{a}/i){r*=b}
}

p r