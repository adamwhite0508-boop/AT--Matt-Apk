use eframe::egui;
use egui::{Color32, RichText, Vec2};
#[derive(PartialEq, Clone)]
enum Screen { Splash, Main }
struct ATWorldMatterApp { screen: Screen, drawer_open: bool, }
impl Default for ATWorldMatterApp {
    fn default() -> Self { Self { screen: Screen::Splash, drawer_open: false } }
}
impl eframe::App for ATWorldMatterApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        let blue = Color32::from_rgb(15, 102, 179);
        if self.drawer_open && self.screen == Screen::Main {
            egui::SidePanel::left("drawer").exact_width(300.0).show(ctx, |ui| {
                egui::Frame::none().fill(blue).inner_margin(20.0).show(ui, |ui|{
                    ui.set_min_height(180.0);
                    ui.vertical_centered(|ui|{
                        ui.label(RichText::new("AT").size(50.0).color(Color32::WHITE).strong());
                        ui.label(RichText::new("AT World Matter").size(18.0).color(Color32::WHITE).strong());
                    });
                });
                ui.add_space(10.0);
                for (icon, text) in [("🧠", "AT BRAIN AI"), ("🖼️", "Photo Poster"), ("🛡️", "AT CROWN Secure"), ("ℹ️", "About Us")]{
                    if ui.add_sized([280.0, 45.0], egui::Button::new(format!("{}  {}", icon, text)).left()).clicked(){ self.drawer_open = false; }
                }
            });
        }
        egui::CentralPanel::default().show(ctx, |ui|{
            match self.screen {
                Screen::Splash => {
                    ui.vertical_centered(|ui|{
                        ui.add_space(80.0);
                        ui.label(RichText::new("Welcome").size(30.0).strong().color(blue));
                        ui.add_space(40.0);
                        let btn = egui::Button::new(RichText::new("Continue to AT World Matter").color(Color32::WHITE)).fill(blue).min_size(Vec2::new(320.0, 48.0)).rounding(8.0);
                        if ui.add(btn).clicked(){ self.screen = Screen::Main; }
                    });
                },
                Screen::Main => {
                    egui::TopBottomPanel::top("top_bar").frame(egui::Frame::none().fill(blue).inner_margin(10.0)).show_inside(ui, |ui|{
                        ui.horizontal(|ui|{
                            if ui.button(RichText::new("☰  MENU").color(Color32::WHITE)).clicked(){ self.drawer_open = !self.drawer_open; }
                            ui.label(RichText::new("AT World Matter").color(Color32::WHITE).strong());
                        });
                    });
                    ui.vertical_centered(|ui|{
                        ui.add_space(100.0);
                        ui.label(RichText::new("✔").size(100.0).color(blue));
                        ui.label(RichText::new("Welcome to AT World Matter").size(24.0).strong());
                    });
                }
            }
        });
    }
}
fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions { viewport: egui::ViewportBuilder::default().with_inner_size([400.0, 750.0]), ..Default::default() };
    eframe::run_native("AT World Matter", options, Box::new(|_| Box::new(ATWorldMatterApp::default())))
}
