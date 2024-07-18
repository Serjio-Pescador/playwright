// @ts-check
import { defineConfig, devices } from '@playwright/test';
const { test, expect } = require('@playwright/test');
const { SlowBuffer } = require('buffer');


test.describe('2.Settings', () => {

  test.beforeEach(async ({ page }, testInfo) => {
    console.log(`Running ${testInfo.title}`);
    await page.goto('http://localhost:5173/');
  });
/*
  test.afterEach(async ({ page }) => {
    expect(await page.screenshot()).toMatchSnapshot({
      maxDiffPixels: 400,    // allow no more than 110 different pixels.
    }); 
  });
*/  
  test('Есть кнопка настройки', async ({ page }) => {
    const settingsButton = page.getByRole('button').nth(1); 
    await settingsButton.hover({ force:true });

    await expect(settingsButton).toBeVisible();  
    await settingsButton.screenshot({ path: './test-results/2.1.settingsbutton.png'});
  });


  test('Тултип у кнопки настройки', async ({ page }) => {
    const settingsButton = page.getByRole('button').nth(1); 
    await settingsButton.hover({ force:true });

    await expect(page.getByRole('tooltip', { name: 'Настройки' })).toBeVisible();
    await page.screenshot({ path: './test-results/2.2.settingsbuttontooltip.png'});
  });


  test('Клик кнопки настройки открывает окно', async ({ page }) => {
    const settingsButton = page.getByRole('button').nth(1); 
    await settingsButton.click();
    const settingWindow = page.locator('.ant-drawer-mask');
    
    await expect(settingWindow).toBeVisible();
    await settingWindow.screenshot({ path: './test-results/2.3.settingsbuttonwindow.png'});
  });


  test('Окно настройки имеет заголовок', async ({ page }) => {
    const settingsButton = page.getByRole('button').nth(1); 
    await settingsButton.click();
    const headSettingWindow = page.getByRole('dialog').locator('div').filter({ hasText: 'Настройки' }).nth(1);
    await headSettingWindow.isVisible();

    await expect(headSettingWindow).toHaveText(/Настройки/);
    await headSettingWindow.screenshot({ path: './test-results/2.4.settingstitle.png'});
  });


  test('Окно настройки имеет кнопку закрыть', async ({ page }) => {
    const settingsButton = page.getByRole('button').nth(1); 
    await settingsButton.click();
    await page.getByLabel('Close', { exact: true }).hover();

    await expect(page.getByLabel('Close', { exact: true })).toBeVisible();
    await page.screenshot({ path: './test-results/2.5.settingclosebutton.png'});
  });
  

  test('кнопка закрыть скрывает окно настроек', async ({ page }) => {
    await page.getByRole('button').nth(1).click();
    await page.getByLabel('Close', { exact: true }).hover();

    const headSettingWindow = page.getByRole('dialog').locator('div').filter({ hasText: 'Настройки' }).nth(1);
    await headSettingWindow.isVisible();
    await page.getByLabel('Close', { exact: true }).click();

    await expect(headSettingWindow).toBeVisible( {visible: false});
    await page.screenshot({ path: './test-results/2.6.settingwindowclose.png'});
  });


  test('Есть чек-бокс 2D-меток в окне настроек', async ({ page }) => {
    await page.getByRole('button').first().click();   
    await page.getByRole('button', { name: 'build' }).click();
    
    await page.getByRole('button', { name: 'tool' }).isVisible();    
    await page.locator('.view > button').first().isVisible();
    await page.locator('.sidebar-footer > button').first().click();
    
    await expect(page.getByLabel('показывать 2D метки помещений').isDisabled()).toBeTruthy();
    await page.screenshot({ path: './test-results/2.7.setting2dmarks.png'});
  });


  test('Установка чек-бокса 2D-меток в окне настроек', async ({ page }) => {
    test.setTimeout(120000);
    await page.getByRole('button').first().click();

    //загрузка демо-модели   
    // await page.getByRole('button', { name: 'build' }).click();
    // await expect(page.getByRole('dialog').locator('div').filter({ hasText: /.ifc/ }).first()).toBeVisible();
    // await page.getByRole('dialog').locator('div').filter({ hasText: /.ifc/} ).first().isHidden();   
  
    //загрузка локального файла
    const fileUpload = page.locator('.upload-file-btn-group > .ant-collapse > .ant-collapse-item > .ant-collapse-content > .ant-collapse-content-box');
    await fileUpload.click();

    await page.setInputFiles('input[type="file"]','./tests/OldBerezin.ifc')
    const dialogWindow = page.getByRole('dialog').locator('div').filter({ hasText: /OldBerezin.ifc/ }).first();
    await dialogWindow.isVisible({timeout: 200});
    await expect(dialogWindow).toHaveText(/OldBerezin.ifc/);


    //ожидание появлегния кнопки тулзов
    await page.getByRole('button', { name: 'tool' }).isVisible(); 

    await page.locator('.sidebar-footer > button').first().click();
    await expect(page.getByRole('dialog').locator('div').filter({ hasText: 'Настройки' }).nth(1)).toBeVisible();
    await page.getByLabel('показывать 2D метки помещений').check();

    await expect(page.getByLabel('показывать 2D метки помещений')).toBeChecked();
    await page.screenshot({ path: './test-results/2.8.setting2dmarkschecked.png'});
  });


  test('Снятие чек-бокса 2D-меток в окне настроек', async ({ page }) => {
    test.setTimeout(120000);
    await page.getByRole('button').first().click();   

    // await page.getByRole('button', { name: 'build' }).click();
    // await page.getByRole('dialog').locator('div').filter({ hasText: /.ifc/}).first();


    //загрузка локального файла
    const fileUpload = page.locator('.upload-file-btn-group > .ant-collapse > .ant-collapse-item > .ant-collapse-content > .ant-collapse-content-box');
    await fileUpload.click();

    await page.setInputFiles('input[type="file"]','./tests/OldBerezin.ifc')
    const dialogWindow = page.getByRole('dialog').locator('div').filter({ hasText: /OldBerezin.ifc/ }).first();
    await dialogWindow.isVisible({timeout: 200});
    await expect(dialogWindow).toHaveText(/OldBerezin.ifc/);


    await page.getByRole('button', { name: 'tool' }).isVisible();    
    await page.locator('.view > button').first().isVisible();
    await page.locator('.sidebar-footer > button').first().click();
    await page.getByLabel('показывать 2D метки помещений').check(); 
    await page.getByLabel('показывать 2D метки помещений').uncheck();

    await expect(await page.getByLabel('показывать 2D метки помещений')).toBeEnabled();
    //await page.getByText('показывать 2D метки помещений').click();
    await page.screenshot({ path: './test-results/2.9.setting2dmarksdisable.png'});
  });


  test('Есть активный чек-бокс комментариев в окне настроек', async ({ page }) => {
    await page.getByRole('button').first().click();   
    await page.getByRole('button', { name: 'build' }).click();
    await page.getByRole('dialog').locator('div').filter({ hasText: /.ifc/ }).first();

    await page.getByRole('button', { name: 'tool' }).isVisible();    
    await page.locator('.view > button').first().isVisible();
    await page.locator('.sidebar-footer > button').first().click();
    
    await expect(page.getByLabel('Всегда отображать комментарии на модели').isDisabled()).toBeTruthy();
    await page.screenshot({ path: './test-results/2.10.settingcomments.png'});
  });


  test('Установка чек-бокса замечаний в окне настроек', async ({ page }) => {
    await page.getByRole('button').first().click();   
    // await page.getByRole('button', { name: 'build' }).click();
    // await page.getByRole('dialog').locator('div').filter({ hasText: /.ifc/ }).first();

    //загрузка локального файла
    await page.setInputFiles('input[type="file"]','./tests/AC20-FZK-Haus.ifc')
    const dialogWindow = page.getByRole('dialog').locator('div').filter({ hasText: 'AC20-FZK-Haus.ifc' }).first();
    await dialogWindow.isVisible({timeout: 200});
    await expect(dialogWindow).toHaveText('AC20-FZK-Haus.ifcОбработка модели');

    await page.getByRole('button', { name: 'tool' }).isVisible();    
    await page.locator('.view > button').first().isVisible();
    await page.locator('.sidebar-footer > button').first().click();
    const settingComments = page.getByLabel('Всегда отображать комментарии на модели');
    await settingComments.isEnabled();
    await settingComments.check();

    await expect(settingComments).toBeChecked();
    await page.screenshot({ path: './test-results/2.11.settingcommentschecked.png'});
  });


  test('Снятие чек-бокса замечаний в окне настроек', async ({ page }) => {
    await page.getByRole('button').first().click();   

    // await page.getByRole('button', { name: 'build' }).click();
    // await page.getByRole('dialog').locator('div').filter({ hasText: /.ifc/ }).first();

    //загрузка локального файла
    await page.setInputFiles('input[type="file"]','./tests/AC20-FZK-Haus.ifc')
    const dialogWindow = page.getByRole('dialog').locator('div').filter({ hasText: 'AC20-FZK-Haus.ifc' }).first();
    await dialogWindow.isVisible({timeout: 200});
    await expect(dialogWindow).toHaveText('AC20-FZK-Haus.ifcОбработка модели');

    await page.getByRole('button', { name: 'tool' }).isVisible();    
    await page.locator('.view > button').first().isVisible();
    await page.locator('.sidebar-footer > button').first().click();
    const settingComments = page.getByLabel('Всегда отображать комментарии на модели');
    await settingComments.isEnabled();
    await settingComments.check();
    await settingComments.uncheck();

    await expect(settingComments).toBeEnabled();
    //await page.getByText('показывать 2D метки помещений').click();
    await page.screenshot({ path: './test-results/2.12.settingcommentsunchecked.png'});
  });


  test('Есть свитч ед.измерения в окне настроек', async ({ page }) => {
    await page.getByRole('button').nth(1).click();

    await expect(page.locator('label').filter({ hasText: 'mm' }).locator('span').first()).toBeVisible();
    await expect(page.locator('label').filter({ hasText: /^m$/ }).locator('span').first()).toBeVisible();
    await page.screenshot({ path: './test-results/2.13.settingsmesureswitch.png'});
  });


  test('изменение ед.измерения в окне настроек', async ({ page }) => {
    await page.getByRole('button').nth(1).click();
    await page.locator('.ant-radio-group').isVisible();

    await page.locator('label').filter({ hasText: /^m$/ }).click();
    // await expect(page.locator('label').filter({ hasText: /^m$/ })).toHaveClass(/ant-radio-button-checked/);
    await expect(page.locator('label').filter({ hasText: /^m$/ })).toBeChecked();
    await page.screenshot({ path: './test-results/2.14.settingsmesurechanged.png'});
  });


  test('переключение обратно ед.измерения в окне настроек', async ({ page }) => {
    await page.getByRole('button').nth(1).click();
    await page.locator('.ant-radio-group').isVisible();

    await page.locator('label').filter({ hasText: /^m$/ }).click();
    await expect(page.locator('label').filter({ hasText: /^m$/ })).toBeChecked();
    await page.locator('label').filter({ hasText: /^mm$/ }).click();
    await expect(page.locator('label').filter({ hasText: /^mm$/ })).toBeChecked();
    await page.screenshot({ path: './test-results/2.15.settingsmesurechanged.png'});
  });
  
  

});