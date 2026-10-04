# SubHunter 🚀

**SubHunter**, hedef sistemlerin gizli alt alan adlarını (subdomain) hızlı ve etkili bir şekilde keşfetmek için Python ile geliştirilmiş hafif bir sızma testi aracıdır. Multi-threading (eşzamanlı iş parçacığı) mimarisi sayesinde DNS kaba kuvvet (brute-force) taramalarını yüksek hızda gerçekleştirir.

## Özellikler ⚡
* **Hızlı Keşif:** Çoklu iş parçacığı desteğiyle yüzlerce alt alan adını saniyeler içinde tarar.
* **Esnek Wordlist Desteği:** İster araç içindeki dahili varsayılan listeyi kullanın ister kendi özel `.txt` wordlist dosyanızı entegre edin.
* **Akıcı Kullanım:** İnteraktif komut satırı arayüzü sayesinde domaini doğrudan terminal içinden kolayca sorgulayın.
* **Sonuç Dışa Aktarma:** Bulunan aktif alt alan adlarını otomatik olarak metin dosyasına kaydedin.

## Kurulum 🛠️

```bash
git clone [https://github.com/Counc/SubHunter.git](https://github.com/Counc/SubHunter.git)
cd SubHunter
pip install -r requirements.txt

