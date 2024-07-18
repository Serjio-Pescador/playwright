// @ts-check
import { defineConfig, devices } from '@playwright/test';
const { test, expect } = require('@playwright/test');
const { SlowBuffer } = require('buffer');


test.describe('1.Files', () => {

  test.beforeEach(async ({ page }, testInfo) => {
    console.log(`Running ${testInfo.title}`);
    await page.goto('http://localhost:5173/');
  });


  // test.afterEach(async ({ page }) => {
  //   expect(await page.screenshot()).toMatchSnapshot({
  //     maxDiffPixels: 400,    // allow no more than 110 different pixels.
  //   }); 
  // });
 
  

  test('Есть кнопка файлы', async ({ page }) => {
    const filesMenuButton = page.getByRole('button').first();
    await expect(filesMenuButton).toBeVisible();  
    await filesMenuButton.screenshot({ path: './test-results/1.1.filesbutton.png'});
  });
  

  test('Есть тултип на кнопке файлы', async ({ page }) => {
    
    await page.getByRole('button').first().hover(); 
    await expect(page.getByRole('tooltip', { name: 'файлы' })).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.2.filesbuttontooltip.png'});
  });


  test('Нажатие на кнопку файлы открывает меню файлов', async ({ page }) => {
     
    await page.getByRole('button').first().click();  
    
    const filesCollapsMenu = page.locator('.upload-file-btn-group > .ant-collapse > .ant-collapse-item > .ant-collapse-content > .ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' })  

    await expect(filesCollapsMenu).toBeVisible();
    await filesCollapsMenu.screenshot({animations: 'disabled', path: './test-results/1.3.filesbuttonmenu.png' });
  });


  test('Есть кнопка назад', async ({ page }) => {
    
    await page.getByRole('button').first().click();
    
    const backButton = page.getByRole('button', { name: 'arrow-left' });
    await expect(backButton).toBeVisible();
    await backButton.screenshot({ path: './test-results/1.4.backbutton.png'});
  });


  test('Есть тултип на кнопке назад', async ({ page }) => {
    
    await page.getByRole('button').first().click();
    await page.getByRole('button', { name: 'arrow-left' }).hover(); 
    
    await expect(page.getByRole('tooltip', { name: 'назад' })).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.5.backbuttontooltip.png'});
  });


  test('Кнопка назад сворачивает меню файлы', async ({ page }) => {
    
    await page.getByRole('button').first().click();
    const filesCollapsMenu = page.locator('.upload-file-btn-group > .ant-collapse > .ant-collapse-item > .ant-collapse-content > .ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' })  

    await page.getByRole('button', { name: 'arrow-left' }).click();

    await expect(page.getByRole('button').first()).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.6.backbuttonclick.png'});
  });


  test('Есть кнопка локально', async ({ page }) => {
   
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();

    //появления кнопок меню файлов
    const filesCollapsMenu = page.locator('.upload-file-btn-group > .ant-collapse > .ant-collapse-item > .ant-collapse-content > .ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' });
    const localUploadButton = page.locator('.ant-collapse-content-box > button').first();

    await localUploadButton.hover();
    await expect(page.getByRole('tooltip', { name: 'локально' })).toBeVisible();
    await localUploadButton.screenshot({ path: './test-results/1.7.localuploadbutton.png'});

  });


  test('Есть тултип на кнопке локально', async ({ page }) => {
      
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();
  
    //появления кнопок меню файлов
    const filesCollapsMenu = page.locator('.upload-file-btn-group > .ant-collapse > .ant-collapse-item > .ant-collapse-content > .ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' })
  
    await page.locator('.ant-collapse-content-box > button').first().hover({ force:true });
    //await page.getByRole('tooltip', { name: 'локально' }).click();
    await expect(page.getByRole('tooltip', { name: 'локально' })).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.8.localbuttontooltip.png'});
    //await page.keyboard.press('Alt+F4');
  });


  test('Есть кнопка удаленно', async ({ page }) => {
    
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();
  
    //появления кнопок меню файлов
    const filesCloud = page.locator('//*[@id="root"]/main/section[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]/div');
    await filesCloud.waitFor({ state: 'visible' })
  
    await filesCloud.hover();
    await expect(page.getByRole('button', { name: 'cloud-download' })).toBeVisible();
    await filesCloud.screenshot({ path: './test-results/1.9.cloudbutton.png'});      
  });


  test('Есть тултип у кнопки удаленно', async ({ page }) => {
          // нажатие кнопки файлы
    await page.getByRole('button').first().click();

    //появления кнопок меню файлов
    const filesCloud = page.locator('//*[@id="root"]/main/section[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]/div');
    await filesCloud.waitFor({ state: 'visible' })

    await filesCloud.hover({ force:true });
    await expect(page.getByRole('tooltip', { name: 'удаленно' })).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.10.cloudbuttontooltip.png'});        
  });


  test('Есть кнопка демо', async ({ page }) => {            
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();   
    const fileDemo = page.getByRole('button', { name: 'build' });
    await fileDemo.waitFor({ state: 'visible' })
        
    await fileDemo.hover({ force:true });
    await expect(fileDemo).toBeVisible();
    await fileDemo.screenshot({ path: './test-results/1.11.demobutton.png'});        
  });


  test('Есть тултип у кнопки демо', async ({ page }) => {            
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();   
    const fileDemo = page.getByRole('button', { name: 'build' });
    await fileDemo.waitFor({ state: 'visible' })
        
    await fileDemo.hover({ force:true });
    await expect(page.getByRole('tooltip', { name: 'демо' })).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.12.demobuttonTooltip.png'});        
  });

  
  test('Есть кнопка сброс', async ({ page }) => {            
    await page.getByRole('button').first().click();  
    
    const filesCollapsMenu = page.locator('.upload-file-btn-group > .ant-collapse > .ant-collapse-item > .ant-collapse-content > .ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' })  

    const fileReset = page.locator('//*[@id="root"]/main/section[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[4]');   
            
    await expect(fileReset).toBeVisible();
    await fileReset.screenshot({ path: './test-results/1.13.resetmenubutton.png' });
    //await page.screenshot({ path: './test-results/1.13.resetmenubutton.png'});        
  });


  test('Загрузка локального файла модели', async ({ page }) => {            
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();   
    const fileUpload = page.locator('.upload-file-btn-group > .ant-collapse > .ant-collapse-item > .ant-collapse-content > .ant-collapse-content-box');
    await fileUpload.click();

    //загрузка локального файла
    await page.setInputFiles('input[type="file"]','./tests/AC20-FZK-Haus.ifc')
    const dialogWindow = page.getByRole('dialog').locator('div').filter({ hasText: 'AC20-FZK-Haus.ifc' }).first();
    await dialogWindow.isVisible({timeout: 200});
    
    await expect(dialogWindow).toHaveText('AC20-FZK-Haus.ifcОбработка модели');
    await dialogWindow.screenshot({animations: 'disabled', path: './test-results/1.14.uploadLocal.png'});        
  });


  test('Загрузка демо файла модели', async ({ page }) => {            
    // нажатие кнопки демо
    await page.getByRole('button').first().click();   
    await page.getByRole('button', { name: 'build' }).click();
    
    const dialogWindow = page.getByRole('dialog').locator('div').filter({ hasText: '.ifc' }).first();
    //await dialogWindow.isVisible({timeout: 200});
    
    await expect(dialogWindow).toHaveText(/.ifc/);
    await dialogWindow.screenshot({animations: 'disabled', path: './test-results/1.15.uploadDemo.png'});        
  });
  
});