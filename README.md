# 用Python來測試接入FB的API吧!
    學習影片: https://www.youtube.com/watch?v=lxUIgZj9wfg&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=19
    學習影片: https://www.youtube.com/watch?v=VXVE9ql85n8&list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF&index=20
    
## 先來了解下FB Graphic API吧!
    FB Graphic API link: https://developers.facebook.com/tools/explorer
    我們用FB登入後，先創建一組應用程式，創建完畢後，右上角點擊工具->圖形API測試工具，就可以進到測試的介面了
    如果找不到，也可以直接用此連結https://developers.facebook.com/tools/explorer/

    
## 實際來請求API接口!
    建議參考圖片哦，FB Graphic operation.png
    1. 先在右側選擇要開啟的權限
    2. 直接點擊GET請求
    3. 左側去新增要請求的參數(要特別注意，需請求的接口資料要開啟權限，否則請求不到東西)
    4. AccessToken要保存好，勿外傳！
    5. 用request.get來請求FB的接口獲取需要的資料吧!

## 成功獲取自己的FB接口資料吧!