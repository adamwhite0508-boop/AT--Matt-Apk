use eframe::egui;
use egui::{Color32, RichText, Vec2};

#[derive(PartialEq, Clone)]
enum Screen { Splash, Main }

struct ATWorldMatterApp { 
    screen: Screen, 
    drawer_open: bool,
    splash_time: f64,
}

impl Default for ATWorldMatterApp {
    fn default() -> Self { 
        Self { 
            screen: Screen::Splash, 
            drawer_open: false,
            splash_time: 0.0,
        } 
    }
}

impl eframe::App for ATWorldMatterApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        let blue = Color32::from_rgb(15, 102, 204);
        
        if self.screen == Screen::Splash {
            self.splash_time += ctx.input(|i| i.unstable_dt as f64);
            if self.splash_time > 2.0 {
                self.screen = Screen::Main;
            }
        }

        if self.drawer_open && self.screen == Screen::Main {
            egui::SidePanel::left("drawer").frame(egui::Frame::none().fill(blue)).show(ctx, |ui| {
                ui.set_min_height(180.0);
                ui.vertical_centered(|ui| {
                    ui.label(RichText::new("AT WORLD").color(Color32::WHITE).size(22.0).strong());
                    ui.label(RichText::new("MATTER").color(Color32::WHITE).size(14.0));
                    if ui.button("Home").clicked() { self.drawer_open = false; }
                    if ui.button("About").clicked() { self.drawer_open = false; }
                });
            });
        }

        egui::CentralPanel::default().frame(egui::Frame::none().fill(blue)).show(ctx, |ui| {
            match self.screen {
                Screen::Splash => {
                    ui.vertical_centered(|ui| {
                        ui.add_space(200.0);
                        ui.label(RichText::new("AT WORLD\nMATTER").color(Color32::WHITE).size(32.0).strong());
                    });
                },
                Screen::Main => {
                    ui.horizontal(|ui| {
                        if ui.button("☰").clicked() { self.drawer_open = !self.drawer_open; }
                        ui.label(RichText::new("AT WORLD MATTER").color(Color32::WHITE).size(20.0).strong());
                    });
                    ui.add_space(20.0);
                    ui.vertical_centered(|ui| {
                        ui.label(RichText::new("Secure App Loaded Successfully!").color(Color32::WHITE).size(18.0));
                    });
                }
            }
        });
        ctx.request_repaint();
    }
}

fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions {
        viewport: egui::ViewportBuilder::default().with_inner_size(Vec2::new(360.0, 740.0)),
        ..Default::default()
    };
    eframe::run_native("AT World Matter", options, Box::new(|_cc| Box::new(ATWorldMatterApp::default())))
}
