// @ts-check
import { defineConfig, devices } from '@playwright/test';
const { test, expect } = require('@playwright/test');
const { SlowBuffer } = require('buffer');


test.describe('1.Files', () => {

  test.beforeEach(async ({ page }, testInfo) => {
    console.log(`Running ${testInfo.title}`);
    await page.goto('http://localhost:4200/');
  });


  // test.afterEach(async ({ page }) => {
  //   expect(await page.screenshot()).toMatchSnapshot({
  //     maxDiffPixels: 400,    // allow no more than 110 different pixels.
  //   }); 
  // });
 
  

  test('Есть кнопка файлы', async ({ page }) => {
    const filesMenuButton = page.locator('.css-dev-only-do-not-override-98ntnt').first();
    await expect(filesMenuButton).toBeVisible(); 
    await filesMenuButton.screenshot({ path: './test-results/1.1.filesbutton.png'});
  });
  

  test('Есть тултип на кнопке файлы', async ({ page }) => {
    
    await page.locator('.css-dev-only-do-not-override-98ntnt').first().hover({ force:true }); 
    // test.setTimeout(300);
    const tooltipFiles = page.getByRole('tooltip', { name: 'файлы' });
    await expect(tooltipFiles).toBeVisible();
    await tooltipFiles.screenshot({animations: 'disabled', path: './test-results/1.2.filesbuttontooltip.png'});
  });


  test('Нажатие на кнопку файлы открывает меню файлов', async ({ page }) => {
     
    await page.locator('.css-dev-only-do-not-override-98ntnt').first().click();  
    
    const filesCollapsMenu = page.locator('.ant-collapse-content-box');
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
    
    await page.locator('.css-dev-only-do-not-override-98ntnt').first().click();
    const filesCollapsMenu = page.locator('.ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' })  

    await page.getByRole('button', { name: 'arrow-left' }).click();

    await expect(page.getByRole('button').first()).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.6.backbuttonclick.png'});
  });


  test('Есть кнопка локально', async ({ page }) => {
   
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();

    //появления кнопок меню файлов
    const filesCollapsMenu = page.locator('.ant-collapse-content-box');
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
    const filesCollapsMenu = page.locator('.ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' });
    const localUploadButton = page.locator('.ant-collapse-content-box > button').first();
  
    await localUploadButton.hover({ force:true });
    await expect(page.getByRole('tooltip', { name: 'локально' })).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.8.localbuttontooltip.png'});

  });


  test('Есть кнопка демо', async ({ page }) => {            
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();   
    const fileDemo = page.getByRole('button', { name: 'build' });
    await fileDemo.waitFor({ state: 'visible' })
        
    await fileDemo.hover({ force:true });
    await expect(fileDemo).toBeVisible();
    await fileDemo.screenshot({ path: './test-results/1.9.demobutton.png'});        
  });


  test('Есть тултип у кнопки демо', async ({ page }) => {            
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();   
    const fileDemo = page.getByRole('button', { name: 'build' });
    await fileDemo.waitFor({ state: 'visible' })
        
    await fileDemo.hover({ force:true });
    await expect(page.getByRole('tooltip', { name: 'демо' })).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/1.10.demobuttonTooltip.png'});        
  });



  test('Загрузка локального файла модели', async ({ page }) => {            
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();

    //появления кнопок меню файлов
    const filesCollapsMenu = page.locator('.ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' });
    const localUploadButton = page.locator('.ant-collapse-content-box > button').first();

    //загрузка локального файла
    await localUploadButton.click();
    await page.setInputFiles('input[type="file"]','./tests/AC20-FZK-Haus.ifc')
    // const dialogWindow = page.getByRole('dialog').locator('div').filter({ hasText: 'AC20-FZK-Haus.ifc' }).first();
    // await dialogWindow.isVisible({timeout: 200});
    // test.setTimeout(600);
    // await expect(dialogWindow).toHaveText('AC20-FZK-Haus.ifcОбработка модели');
    await page.screenshot({animations: 'disabled', path: './test-results/1.11.uploadLocal.png'});        
  });


  test('Есть кнопка сброс', async ({ page }) => {            
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();

    //появления кнопок меню файлов
    const filesCollapsMenu = page.locator('.ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' });
    const localUploadButton = page.locator('.ant-collapse-content-box > button').first();

    //загрузка локального файла
    await localUploadButton.click();
    await page.setInputFiles('input[type="file"]','./tests/AC20-FZK-Haus.ifc')

    const fileReset = page.locator('button:nth-child(4)').first();
    await expect(fileReset).toBeVisible();
    await fileReset.screenshot({ path: './test-results/1.12.resetmenubutton.png' });      
  });


  test('У кнопка сброс есть тултип', async ({ page }) => {            
    // нажатие кнопки файлы
    await page.getByRole('button').first().click();

    //появления кнопок меню файлов
    const filesCollapsMenu = page.locator('.ant-collapse-content-box');
    await filesCollapsMenu.waitFor({ state: 'visible' });
    const localUploadButton = page.locator('.ant-collapse-content-box > button').first();
    
    //загрузка локального файла
    await localUploadButton.click();
    await page.setInputFiles('input[type="file"]','./tests/AC20-FZK-Haus.ifc')

    await page.locator('button:nth-child(4)').first().hover({ force:true });
    const resetTooltip = page.getByRole('tooltip', { name: 'Закрыть' });
    await expect(page.getByRole('tooltip', { name: 'Закрыть' })).toBeVisible();
    await resetTooltip.screenshot({ path: './test-results/1.13.resetmenubuttontooltip.png' });      
  });

  // test('Загрузка демо файла модели', async ({ page }) => {            
  //   // нажатие кнопки демо
  //   await page.getByRole('button').first().click();   
  //   await page.getByRole('button', { name: 'build' }).click();
    
  //   const dialogWindow = page.getByRole('dialog').locator('div').filter({ hasText: '.ifc' }).first();
  //   //await dialogWindow.isVisible({timeout: 200});
    
  //   await expect(dialogWindow).toHaveText(/.ifc/);
  //   await dialogWindow.screenshot({animations: 'disabled', path: './test-results/1.15.uploadDemo.png'});        
  // });
  
});