// @ts-check
import { defineConfig, devices } from '@playwright/test';
const { test, expect } = require('@playwright/test');
const { SlowBuffer } = require('buffer');
const { TIMEOUT } = require('dns');


test.describe('3.Help', () => {

  test.beforeEach(async ({ page }, testInfo) => {
    console.log(`Running ${testInfo.title}`);
    await page.goto('http://localhost:5173/');
  });


  // test.afterEach(async ({ page }) => {
  //   expect(await page.screenshot()).toMatchSnapshot({
  //     maxDiffPixels: 800,    // allow no more than 110 different pixels.
  //   }); 
  // });


  test('Есть кнопка помощь', async ({ page }) => {
    const helpButton = page.getByRole('button').nth(2); 
    await helpButton.hover({ force:true });

    await expect(helpButton).toBeVisible();  
    await helpButton.screenshot({animations: 'disabled', path: './test-results/3.1.helpbutton.png'});
  });


  test('Тултип у кнопки помощь', async ({ page }) => {
    const helpButton = page.getByRole('button').nth(2); 
    await helpButton.hover({ force:true });

    await expect(page.getByRole('tooltip', { name: 'Помощь' })).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.2.helpbuttontooltip.png'});
  });


  test('Клик кнопки помощь открывает окно', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    const heplWindow = page.getByText('Помощь123456CancelOK');
    test.setTimeout(6000);

    await expect(heplWindow).toBeVisible();
    await heplWindow.screenshot({animations: 'disabled', path: './test-results/3.3.helpwindow.png'});
  });


  test('Окно Помощь имеет заголовок', async ({ page }) => {
    const helpButton = page.getByRole('button').nth(2); 
    await helpButton.click();
    const headHelpWindow = page.getByRole('heading', { name: 'Помощь' });
    test.setTimeout(6000);
    await headHelpWindow.isVisible();

    await expect(headHelpWindow).toHaveText(/Помощь/);
    await headHelpWindow.screenshot({animations: 'disabled', path: './test-results/3.4.helptitle.png'});
  });


  test('окно помощь имеет кнопку Х закрыть', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    const closehelpbutton = page.getByLabel('Close', { exact: true });
    await closehelpbutton.hover();
    test.setTimeout(6000);

    await expect(closehelpbutton).toBeVisible();
    await page.screenshot({ path: './test-results/3.5.closewindowcross.png'});
  });


  test('кнопка закрыть скрывает окно помощь', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    const closehelpbutton = page.getByLabel('Close', { exact: true });
    await closehelpbutton.click();

    await expect(page.locator('div').filter({ hasText: 'Помощь123456CancelOK' }).nth(2)).toBeVisible( {visible: false});
    await page.screenshot({animations: 'disabled', path: './test-results/3.6.helpwindowclose.png'});
  });


  // test('клик за пределами окна скрывает окно помощь', async ({ page }) => {
  //   await page.getByRole('button').nth(2).click();
  //   const heplWindow = page.locator("/html/body/div[4]/div/div[2]/div");    
    
  //   await page.getByRole('button').nth(2).click();
  //   await expect(page.locator('div').filter({ hasText: 'Помощь123456CancelOK' }).nth(2)).toBeVisible( {visible: false});
  //   await page.screenshot({path: './test-results/3.7.helpwindowclose.png'});
  // });


  test('окно помощь открывает слайд 1', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    await page.locator("body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content").isVisible();  

    await expect(page.locator('div:nth-child(2) > div > ._card_h6omr_1 > img')).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.8.helpwindowslide1.png'});
  });


  test('окно помощь имеет слайд 2', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    await page.locator('div:nth-child(2) > div > ._card_h6omr_1 > img').isVisible();  
    await page.getByRole('button', { name: '2' }).click();
    test.setTimeout(6000);

    await expect(page.locator('div:nth-child(3) > div > ._card_h6omr_1 > img')).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.9.helpwindowslide2.png'});
  });


  test('окно помощь имеет слайд 3', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    await page.locator('div:nth-child(2) > div > ._card_h6omr_1 > img').isVisible();  
    await page.getByRole('button', { name: '3' }).click();
    test.setTimeout(6000);

    await expect(page.locator('div:nth-child(4) > div > ._card_h6omr_1 > img')).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.10.helpwindowslide3.png'});
  });


  test('окно помощь имеет слайд 4', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    await page.locator('div:nth-child(2) > div > ._card_h6omr_1 > img').isVisible();  
    await page.getByRole('button', { name: '4' }).click();
    test.setTimeout(12000);

    await expect(page.locator('div:nth-child(5) > div > ._card_h6omr_1 > img')).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.11.helpwindowslide4.png'});
  });

  
  test('окно помощь имеет слайд 5', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    await page.locator('div:nth-child(2) > div > ._card_h6omr_1 > img').isVisible();  
    await page.getByRole('button', { name: '5' }).click();

    await expect(page.locator('div:nth-child(6) > div > ._card_h6omr_1 > img')).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.12.helpwindowslide5.png'});
  });


  test('окно помощь имеет слайд 6', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    await page.locator('div:nth-child(2) > div > ._card_h6omr_1 > img').isVisible();  
    await page.getByRole('button', { name: '6' }).click();
    test.setTimeout(12000);

    await expect(page.locator('div:nth-child(7) > div > ._card_h6omr_1 > img')).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.13.helpwindowslide6.png'});
  });


  test('окно помощь перематывает слайды влево', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    await page.locator('div:nth-child(2) > div > ._card_h6omr_1 > img').isVisible();  
    await page.getByRole('button', { name: 'left' }).click();
    await page.getByRole('button', { name: 'left' }).click();
    await page.getByRole('button', { name: 'left' }).click();

    const slide = page.locator('div:nth-child(5) > div > ._card_h6omr_1 > img');
    await expect(slide).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.14.helpwindowleft.png'});
  });

  
    test('окно помощь перематывает слайды вправо', async ({ page }) => {
    await page.getByRole('button').nth(2).click();
    await page.locator('div:nth-child(2) > div > ._card_h6omr_1 > img').isVisible();  
    await page.getByRole('button', { name: 'right' }).click();
    await page.getByRole('button', { name: 'right' }).click();
    await page.getByRole('button', { name: 'right' }).click();

    const slide = page.locator('div:nth-child(5) > div > ._card_h6omr_1 > img');
    await expect(slide).toBeVisible();
    await page.screenshot({animations: 'disabled', path: './test-results/3.15.helpwindowright.png'});
  });




});