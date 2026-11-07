use eframe::egui;

#[derive(Default)]
struct App {
    name: String,
    counter: i32,
    slider: f32,
    checked: bool,
}

impl eframe::App for App {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("AT World Matter");
            ui.separator();
            ui.label("Welcome! App chal raha hai.");

            ui.separator();
            ui.horizontal(|ui| {
                ui.label("Name:");
                ui.text_edit_singleline(&mut self.name);
            });

            ui.separator();
            if ui.button(format!("Click Count: {}", self.counter)).clicked() {
                self.counter += 1;
            }

            ui.separator();
            ui.add(egui::Slider::new(&mut self.slider, 0.0..=100.0).text("Slider"));

            ui.separator();
            ui.checkbox(&mut self.checked, "Enable Feature");

            if self.checked {
                ui.label(format!("Hello {}, Slider = {:.0}", self.name, self.slider));
            }
        });
    }
}

#[cfg(not(target_os = "android"))]
fn main() {
    let options = eframe::NativeOptions::default();
    let _ = eframe::run_native(
        "AT World Matter",
        options,
        Box::new(|_cc| Ok(Box::<App>::default())),
    );
}

#[cfg(target_os = "android")]
use android_logger::Config;
#[cfg(target_os = "android")]
use android_activity::AndroidApp;

#[cfg(target_os = "android")]
#[no_mangle]
pub fn android_main(app: AndroidApp) {
    android_logger::init_once(Config::default().with_tag("AT_MATT"));
    let options = eframe::NativeOptions {
        event_loop_builder: Some(Box::new(|builder| {
            builder.with_android_app(app.clone());
            Ok(builder)
        })),
        ..Default::default()
    };

    let _ = eframe::run_native(
        "AT World Matter",
        options,
        Box::new(|_cc| Ok(Box::<App>::default())),
    );
}
