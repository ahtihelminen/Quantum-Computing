import pygame
import sys
from cirq import *

class GUI:
    def __init__(self, rows, cols, n_moments, circuit=None):
        pygame.init()
        
        self.circuit = circuit

        # calculation parameters
        self.rows = rows
        self.cols = cols
        self.n_moments = n_moments-1
        self.current_moment = 0
        
        # object sizes
        self.cell_size = 100
        self.slider_width = 300
        self.slider_height = 30
        
        # Window dimensions
        self.margin_x = 200
        self.margin_y = 100
        self.width = cols * self.cell_size + 2*self.margin_x
        self.height = rows * self.cell_size + 2*self.margin_y

        # Colors
        self.bg_color = (30, 30, 30)
        self.grid_color = (200, 200, 200)
        self.slider_color = (100, 100, 255)
        self.text_color = (0, 0, 0)
        self.line_color = (100, 100, 100)

        
        # Set up screen and fonts
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Quantum Circuit Visualization")
        self.font = pygame.font.SysFont(None, 24)
        
        # Slider properties
        self.slider_rect = pygame.Rect((self.width - self.slider_width) // 2,
                                       self.height - 50,
                                       self.slider_width,
                                       self.slider_height
                                       )
        self.slider_position = self.slider_rect.x
        
    
    def draw_AOD(self):
        pass

    def draw_SLM(self):
        pass
    
    def draw_grid(self):
        center_x = self.width//2
        grid_width = self.cols * self.cell_size
        grid_shift_x = self.margin_x + self.cell_size//2
        grid_shift_y = self.margin_y + self.cell_size//2
        
        text_shift_x = self.margin_x-50
        text_shift_y = self.margin_y*2//3
        self.qubit_positions = [[0 for n in range(self.cols)] for m in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                qubit_x = grid_shift_x + col * self.cell_size
                qubit_y = grid_shift_y + row * self.cell_size
                pygame.draw.circle(self.screen,
                                   (120,20,0),
                                   (qubit_x,
                                    qubit_y),
                                    20)
                self.qubit_positions[row][col] = (qubit_x, qubit_y)

         # Draw row numbers and grid lines
        for row in range(self.rows):
            row_text = self.font.render(str(row), True, self.grid_color)
            self.screen.blit(row_text, (text_shift_x, row * self.cell_size + grid_shift_y - row_text.get_height() // 2))
            
        for col in range(self.cols):
            col_text = self.font.render(str(col), True, self.grid_color)
            self.screen.blit(col_text, (col * self.cell_size + grid_shift_x - col_text.get_width() // 2, text_shift_y))

    def draw_gates(self):
        for n, moment in enumerate(self.circuit):
            if n == self.current_moment:
                for operation in moment:
                    if isinstance(operation.gate, type(CNOT)):
                        control, target = operation.qubits
                        control_text = self.font.render('@', True, self.grid_color)
                        control_x = self.qubit_positions[control.row][control.col][0]
                        control_y = self.qubit_positions[control.row][control.col][1]
                        
                        target_text = self.font.render('X', True, self.grid_color)
                        target_x = self.qubit_positions[target.row][target.col][0]
                        target_y = self.qubit_positions[target.row][target.col][1]
                        
                        pygame.draw.line(
                            self.screen,
                            self.line_color,
                            (control_x, control_y),
                            (target_x, target_y),
                            2
                        )
                        
                        self.screen.blit(control_text, (
                                                    control_x - control_text.get_width()//2,
                                                    control_y - control_text.get_height()//2
                                                    )
                        )
                        self.screen.blit(target_text, (
                                                    target_x - target_text.get_width()//2,
                                                    target_y - target_text.get_height()//2
                                                    )
                        )

                    elif isinstance(operation.gate, type(SWAP)):
                        q1, q2 = operation.qubits
                        text = self.font.render('x', True, self.grid_color)
                        q1_x = self.qubit_positions[q1.row][q1.col][0]
                        q1_y = self.qubit_positions[q1.row][q1.col][1]
                        
                        q2_x = self.qubit_positions[q2.row][q2.col][0]
                        q2_y = self.qubit_positions[q2.row][q2.col][1]
                        
                        pygame.draw.line(
                            self.screen,
                            self.line_color,
                            (q1_x, q1_y),
                            (q2_x, q2_y),
                            2
                        )
                        
                        self.screen.blit(text, (
                                                q1_x - text.get_width()//2,
                                                q1_y - text.get_height()//2
                                                )
                        )
                        self.screen.blit(text,(
                                                q2_x - text.get_width()//2,
                                                q2_y - text.get_height()//2
                                                )
                        )
                        
                    else:
                        qubit = operation.qubits[0]
                        gate_text = self.font.render(str(operation.gate), True, self.grid_color)
                        self.screen.blit(gate_text, (
                                                    self.qubit_positions[qubit.row][qubit.col][0]-gate_text.get_width()//2,
                                                    self.qubit_positions[qubit.row][qubit.col][1]-gate_text.get_height()//2
                                                    ))

    def draw_slider(self):
        """Draws the slider for selecting moments."""
        # Draw slider background
        pygame.draw.rect(self.screen, (100, 100, 100), self.slider_rect, border_radius = 15)
        # Calculate the handle position based on current moment
        handle_x = 15 + self.slider_rect.x + (self.current_moment / (self.n_moments - 1)) * (self.slider_width-30)
        pygame.draw.circle(self.screen, self.slider_color, (int(handle_x), self.slider_rect.centery), 15)

        # Display the moment number
        moment_text = self.font.render(f"Moment: {self.current_moment + 1}", True, self.grid_color)
        self.screen.blit(moment_text, (self.slider_rect.x, self.slider_rect.y - 30))
        
    def update_moment(self, pos_x):
        """Updates the current moment based on slider position."""
        if pos_x == 'LEFT':
            self.current_moment = max(0, self.current_moment-1)
        elif pos_x == 'RIGHT':
            self.current_moment = min(self.current_moment+1, self.n_moments-1)
        else:            
            relative_x = pos_x - self.slider_rect.x
            moment = int((relative_x / self.slider_width) * (self.n_moments - 1))
            self.current_moment = max(0, min(self.n_moments - 1, moment))

    def run(self):
        """Main loop for the Pygame GUI."""
        running = True
        dragging = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.slider_rect.collidepoint(event.pos):
                        dragging = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragging = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.update_moment('LEFT')
                    elif event.key == pygame.K_RIGHT:
                        self.update_moment('RIGHT')
                elif event.type == pygame.MOUSEMOTION and dragging:
                    self.update_moment(event.pos[0])

            # Clear the screen
            self.screen.fill(self.bg_color)
            
            # Draw the grid and slider
            self.draw_grid()
            self.draw_slider()
            if self.circuit is not None:
                self.draw_gates()
            
            
            # Update display
            pygame.display.flip()
        
        # Quit Pygame
        pygame.quit()
        sys.exit()
