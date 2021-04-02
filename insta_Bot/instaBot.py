from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from time import sleep
import sys
usr=""
username=""
passwd=""
class InstaBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_extension('./extensions/Extension for Instagram.crx')
        self.driver = webdriver.Chrome("./drivers/chromedriver_89",chrome_options=options) 
        # self.driver = webdriver.Firefox("./drivers/firefoxdriver.exe")
        self.driver.get("https://instagram.com")
        sleep(5)
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/div[2]/button")\
                .click()
            sleep(3);
        except:
            pass
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(passwd)
        try:
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
        except:
            pass
        sleep(4)
        self.driver.find_element_by_xpath('//button[contains(text(),"Not Now")]')\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath('//button[contains(text(),"Not Now")]')\
            .click()
        sleep(1)   
        self.driver.find_element_by_xpath('//input[@placeholder="Search"]')\
            .send_keys(usr)
        sleep(10)
        self.driver.find_element_by_xpath('//a[@class="-qQT3"]')\
            .click()
        sleep(15)
    
    def get_int(self,n):
        ans=0.0
        div=-1
        mul=0
        for i in n:
            if i=='f':
                break;
            try:
                t=int(i)
                ans*=10;
                ans+=t;
                if(div!=-1):
                    div+=1
            except:
                if(i=='.'):
                    div=0
                if(i=='K' or i=='k'):
                    mul=3
                if(i=='M' or i=='m'):
                    mul=6
        if(div==-1):
            div=0;
        ans*=10**(mul-div);
        return int(ans)

    def get_unfollowers(self,name):
        no_fllwig=self.get_int(self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").text)
        no_fllwers=self.get_int(self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").text)
        print("followers=",no_fllwers,"following=",no_fllwig)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(7)
        following = self._get_names(no_fllwig)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names(no_fllwers)
        not_following_back = [str(user) for user in following if user not in followers]
        you_not_following_back=[str(user) for user in followers if user not in following]
        sleep(3)
        self.driver.find_element_by_xpath('//a[contains(@href,"/direct/inbox/")]')\
            .click()
        sleep(7)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//input[contains(@name,'queryBox')]")\
            .send_keys(name)
        sleep(5)
        self.driver.find_element_by_xpath('//button[contains(@class,"dCJp8 ")]')\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath('//div[contains(text(),"Next")]')\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Message...")]')\
            .click()
        sleep(1)
        s="inko unfollow kr do frands :\n";
        for i in not_following_back:
                s+=i+"\n";
        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Message...")]')\
                .send_keys(s)
        sleep(1)
        try:
            self.driver.find_element_by_xpath('//button[contains(text(),"Send")]')\
                .click()
        except:
            pass
        s="inko bhi follow kr do frands :\n";
        for i in you_not_following_back:
                s+=i+"\n";
        self.driver.find_element_by_xpath('//textarea[contains(@placeholder,"Message...")]')\
                .send_keys(s)
        sleep(1)
        try:
            self.driver.find_element_by_xpath('//button[contains(text(),"Send")]')\
                .click()
        except:
            pass
        sleep(7)
        self.driver.quit()

    def _get_names(self,n):
        sleep(10)
        scroll_box = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        last_ht, ht = 0, 1
        links=();
        while(1==1) :
            last_ht = ht
            sleep(3)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
            if(last_ht==ht):
                links = scroll_box.find_elements_by_tag_name('a')
                names = [name.text for name in links if name.text != '']
                if(len(names)>=n-1):
                    print("read total of",len(names))
                    break;
                print("seems you have a naggy network got only",len(names),"out of",n)

        names = [name.text for name in links if name.text != '']
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names
usr=""
if(len(sys.argv)==1):
    print("Enter yur username ");
    username=sys.stdin.readline();
    print("Enter your password ");
    passwd=sys.stdin.readline();
    print("Enter the users Instagram id  whose not following back list you want (can be your usename itself too) ");
    usr=sys.stdin.readline();
else:
    usr=sys.argv[1]
my_bot = InstaBot()
my_bot.get_unfollowers(usr)
